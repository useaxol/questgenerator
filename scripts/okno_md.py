"""Parser do formato intermediário de questionários okno (.md).

Formato descrito em .claude/skills/okno-questionario/references/formato-markdown.md.
Usado por checar_questionario.py e gerar_docx.py.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

QID_RE = re.compile(
    r"^###\s+((?:P|Q)\.\s?\d+[A-Za-z]?(?:_\d+)?|[A-L]\.|S\d+\.?)\s*(.*)$"
)
INSTR_PREFIXES = (
    "PROGRAMAÇÃO", "PROGRAMACAO", "PROGRAMADOR", "PROGRAMMING", "PROG:", "PN:", "PN ",
    "ENTREVISTADOR", "INTERVIEWER", "PROCESSAMENTO", "MODERADOR",
    "NOVA TELA", "NEW SCREEN", "APLICAR", "APPLY", "SOMENTE", "ONLY", "DEVE ", "MUST ",
    "SE ", "IF ", "SHOW ", "MOSTRAR ", "PERGUNTAR ", "REPETIR", "REPEAT", "ATENÇÃO", "ATTENTION",
)
SECTION_RE = re.compile(r"^##\s+(.*)$")


def norm_qid(raw: str) -> str:
    """'P.64A' -> '64A', 'Q. 4a' -> '4A', 'A.' -> 'A', 'S1.' -> 'S1'."""
    raw = raw.strip().rstrip(".")
    m = re.match(r"^[PQ]\.\s?(.+)$", raw)
    if m:
        raw = m.group(1)
    return raw.upper()


@dataclass
class Table:
    header: list[str]
    rows: list[list[str]]
    line: int


@dataclass
class Question:
    qid: str          # normalizado
    label: str        # como escrito (P.9)
    text: str         # enunciado
    line: int
    section: str
    index: int
    pre_lines: list[tuple[int, str]] = field(default_factory=list)   # instruções antes do ###
    body_lines: list[tuple[int, str]] = field(default_factory=list)  # texto/instruções depois do ###
    tables: list[Table] = field(default_factory=list)
    new_screen: bool = False


@dataclass
class Section:
    name: str
    line: int
    kind: str  # intro | cotas | secao | encerramento | mapa | outro
    lines: list[tuple[int, str]] = field(default_factory=list)
    tables: list[Table] = field(default_factory=list)


@dataclass
class Doc:
    meta: dict
    sections: list[Section]
    questions: list[Question]
    lines: list[str]

    def by_id(self) -> dict[str, Question]:
        return {q.qid: q for q in self.questions}


def parse_frontmatter(lines: list[str]) -> tuple[dict, int]:
    if not lines or lines[0].strip() != "---":
        return {}, 0
    meta: dict = {}
    for i in range(1, len(lines)):
        s = lines[i].rstrip("\n")
        if s.strip() == "---":
            return meta, i + 1
        s = s.split(" #", 1)[0]
        if ":" in s:
            k, v = s.split(":", 1)
            v = v.strip().strip('"').strip("'")
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip('"\'') for x in v[1:-1].split(",") if x.strip()]
            meta[k.strip()] = v
    return meta, 0


def split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    # respeita \| escapado
    parts = re.split(r"(?<!\\)\|", s)
    return [p.strip().replace("\\|", "|") for p in parts]


def is_sep_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{2,}:?", c or "---") for c in cells)


def section_kind(name: str) -> str:
    n = name.upper()
    if n.startswith("INTRODU"):
        return "intro"
    if n.startswith("COTAS") or n.startswith("QUOTA"):
        return "cotas"
    if n.startswith("ENCERRAMENTO") or n.startswith("CLOSING"):
        return "encerramento"
    if n.startswith("MAPA DE COBERTURA"):
        return "mapa"
    if n.startswith("SEÇÃO") or n.startswith("SECAO") or n.startswith("SECTION"):
        return "secao"
    return "outro"


def is_instruction(s: str) -> bool:
    t = s.strip().lstrip("(").upper()
    return t.startswith(INSTR_PREFIXES)


def parse(path: str | Path) -> Doc:
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    meta, start = parse_frontmatter(lines)

    sections: list[Section] = []
    questions: list[Question] = []
    cur_sec: Section | None = None
    cur_q: Question | None = None
    pending: list[tuple[int, str]] = []
    pending_screen = False
    after_table = False
    tbl_rows: list[list[str]] = []
    tbl_start = 0

    def flush_table():
        nonlocal tbl_rows, after_table
        if not tbl_rows:
            return
        header = tbl_rows[0]
        body = [r for r in tbl_rows[1:] if not is_sep_row(r)]
        t = Table(header=header, rows=body, line=tbl_start)
        if cur_q is not None and cur_sec is not None and cur_q.section == cur_sec.name:
            cur_q.tables.append(t)
        elif cur_sec is not None:
            cur_sec.tables.append(t)
        tbl_rows = []
        after_table = True

    for ln0, raw in enumerate(lines[start:], start=start + 1):
        s = raw.rstrip()
        if s.strip().startswith("|"):
            if not tbl_rows:
                tbl_start = ln0
            tbl_rows.append(split_row(s))
            continue
        flush_table()

        m = SECTION_RE.match(s)
        if m and not s.startswith("###"):
            name = m.group(1).strip()
            cur_sec = Section(name=name, line=ln0, kind=section_kind(name))
            sections.append(cur_sec)
            cur_q = None
            pending = []
            pending_screen = False
            after_table = False
            if cur_sec.kind == "mapa":
                break
            continue

        mq = QID_RE.match(s)
        if mq:
            label, qtext = mq.group(1), mq.group(2).strip()
            q = Question(
                qid=norm_qid(label), label=label.rstrip("."), text=qtext, line=ln0,
                section=cur_sec.name if cur_sec else "", index=len(questions),
                pre_lines=pending, new_screen=pending_screen,
            )
            questions.append(q)
            cur_q = q
            pending = []
            pending_screen = False
            after_table = False
            continue

        if s.startswith("###"):  # subtítulo não-pergunta (roteiro quali)
            cur_q = None
            pending = []
            after_table = False
            if cur_sec:
                cur_sec.lines.append((ln0, s))
            continue

        if not s.strip():
            continue

        up = s.strip().upper()
        if up.startswith("NOVA TELA") or up.startswith("NEW SCREEN"):
            pending_screen = True
            pending.append((ln0, s.strip()))
            after_table = True  # o que vier depois pertence à próxima pergunta
            continue

        if cur_q is not None and not after_table:
            cur_q.body_lines.append((ln0, s.strip()))
        elif cur_q is not None and after_table:
            pending.append((ln0, s.strip()))
        if cur_sec is not None:
            cur_sec.lines.append((ln0, s.strip()))
    flush_table()

    return Doc(meta=meta, sections=sections, questions=questions, lines=lines)


def option_rows(t: Table) -> list[dict]:
    """Interpreta tabela Opção | Cód | Ação (ou variações)."""
    hdr = [h.lower() for h in t.header]
    code_idx = None
    act_idx = None
    for i, h in enumerate(hdr):
        if code_idx is None and h in ("cód", "cod", "código", "codigo", "code", "cód."):
            code_idx = i
        if act_idx is None and h in ("ação", "acao", "action", "roteamento", "routing"):
            act_idx = i
    out = []
    if code_idx is None:
        return out
    for r in t.rows:
        r = r + [""] * (len(t.header) - len(r))
        out.append({
            "label": r[0] if code_idx != 0 else r[1],
            "code": r[code_idx].strip(),
            "action": r[act_idx].strip() if act_idx is not None else None,
            "cells": r,
        })
    return out


def combined_columns(t: Table) -> list[tuple[int, str]]:
    """Colunas que são perguntas (P.16, Q.19...) numa tabela combinada."""
    cols = []
    for i, h in enumerate(t.header):
        m = re.fullmatch(r"\s*([PQ]\.\s?\d+[A-Za-z]?)\s*", h)
        if m:
            cols.append((i, norm_qid(m.group(1))))
    return cols
