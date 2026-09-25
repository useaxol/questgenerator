#!/usr/bin/env python3
"""Checador determinístico de questionários okno (formato intermediário .md).

Uso:
    python3 scripts/checar_questionario.py projetos/<slug>/<arquivo>.md [--json]

Saída: relatório com ERRO / ALERTA / INFO. Código de saída 1 se houver ERRO.
Não substitui o analista sênior — é a primeira peneira (pulos, referências, placeholders,
blocos fixos, escalas, códigos e maiúsculas).
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from okno_md import Doc, combined_columns, is_instruction, option_rows, parse  # noqa: E402

REF_RE = re.compile(r"(?<![A-Za-z])([PQ])\.?\s?(\d+[A-Za-z]?)(?![\d])")
LETTER_REF_RE = re.compile(r"(?<![A-Za-z])[PQ]\.([A-L])(?![A-Za-z])")
SKIP_RE = re.compile(
    r"(PULE|PULAR|PULA|V[ÁA]|SKIP|GO)\s+(?:PARA|TO|A)?\s*(?:A\s+)?([PQ])\.?\s?(\d+[A-Za-z]?)",
    re.IGNORECASE,
)
FORWARD_OK_RE = re.compile(
    r"APLICAR|APPLY|REPETIR|REPEAT|BLOCO|BLOCK|MOVED|PLACE|TRANSFER|TRANSPORT|AUTO ?PUNCH|"
    r"ASSINALAR|SELECT CODE|PUNCH|CHECK|RODIZIAR .* E |RANDOMIZE .* AND|ORDEM D",
    re.IGNORECASE,
)
TYPE_CODE_RE = re.compile(
    r"\((RU|RM|SC|MC|ESPONT[ÂA]NEO|ESPONTANEA|ESPONTÂNEA|SPONTANEOUS|RU POR|RM POR|SC PER|MC PER|NUM[ÉE]RICA|"
    r"ABERTA|OE)[^)]*\)|\[(SS|MS|OE|OEN|TT\d)[^\]]*\]|RU POR|SC PER|MC PER|\(RU\b|\(RM\b",
    re.IGNORECASE,
)
PLACEHOLDERS = [
    ("CONTINUAR OU ENCERRAR", "ERRO"),
    ("[INSERIR", "ALERTA"),
    ("[A DEFINIR", "ALERTA"),
    ("[PERSONALIZAR", "ERRO"),
    ("XXX", "ALERTA"),
]

STD_SCALES = {
    "Aceitação (passado)": ["não gostei nada", "não gostei", "nem gostei nem desgostei", "gostei", "gostei muito"],
    "Aceitação (presente)": ["não gosto nada", "não gosto", "nem gosto nem desgosto", "gosto", "gosto muito"],
    "Intenção de compra": ["certamente não compraria", "provavelmente não compraria", "não tenho certeza",
                           "provavelmente compraria", "certamente compraria"],
    "Satisfação": ["totalmente insatisfeito(a)", "insatisfeito(a)", "nem insatisfeito(a) nem satisfeito(a)",
                   "satisfeito(a)", "totalmente satisfeito(a)"],
    "Concordância": ["discordo totalmente", "discordo", "nem concordo nem discordo", "concordo",
                     "concordo totalmente"],
    "Qualidade": ["péssimo", "ruim", "nem bom nem ruim", "bom", "excelente"],
    "Adequação": ["muito inadequada", "inadequada", "mais ou menos adequada", "adequada", "muito adequada"],
    "Diferenciação": ["nada diferente", "um pouco diferente", "mais ou menos diferente", "diferente",
                      "muito diferente"],
}
SCALE_ALIASES = {
    "não tenho certeza se compraria": "não tenho certeza",
    "totalmente insatisfeito": "totalmente insatisfeito(a)",
    "insatisfeito": "insatisfeito(a)",
    "satisfeito": "satisfeito(a)",
    "totalmente satisfeito": "totalmente satisfeito(a)",
    "nem insatisfeito nem satisfeito": "nem insatisfeito(a) nem satisfeito(a)",
}
QUANTI_TYPES_WITH_SCREENER = (
    "quanti-adhoc", "quanti-teste-produto-recrutamento", "quanti-teste-embalagem", "quanti-teste-comunicacao",
    "quanti-tracking", "quali-recrutamento",
)
SCREEN_SECTION_WORDS = ("TRIAGEM", "FILTRO", "RECRUTAMENTO", "SCREENER", "SCREENING", "RECRUITMENT")


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def norm_label(s: str) -> str:
    s = re.sub(r"\s+", " ", s.strip().lower().replace("**", ""))
    s = s.rstrip(".")
    return SCALE_ALIASES.get(s, s)


class Report:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, level: str, where: str, msg: str) -> None:
        self.items.append({"nivel": level, "onde": where, "msg": msg})

    def count(self, level: str) -> int:
        return sum(1 for i in self.items if i["nivel"] == level)


def uppercase_violation(line: str) -> bool:
    """Instrução deve estar em maiúsculas (ignora trechos entre aspas e itens de lista de preço/códigos)."""
    body = re.sub(r"[\"“'‘][^\"”'’]*[\"”'’]", "", line)
    body = re.sub(r"\[[^\]]*\]", "", body)
    letters = [c for c in body if c.isalpha()]
    if len(letters) < 6:
        return False
    lower = sum(1 for c in letters if c.islower())
    return lower / len(letters) > 0.15


def refs_in(text: str) -> list[str]:
    return [(m.group(2)).upper() for m in REF_RE.finditer(text)]


def check(doc: Doc) -> Report:
    rep = Report()
    meta = doc.meta
    tipo = str(meta.get("tipo", "")).lower()
    modo = str(meta.get("modo", "")).lower()
    is_roteiro = tipo in ("quali-roteiro", "quali-pre-tarefa")

    # ---------- frontmatter
    if not meta:
        rep.add("ERRO", "frontmatter", "Frontmatter ausente (job, estudo, titulo, tipo, entrevistas, data, idioma, modo).")
    else:
        for k in ("job", "estudo", "titulo", "tipo", "data", "idioma", "modo"):
            if not meta.get(k):
                rep.add("ALERTA", "frontmatter", f"Campo '{k}' vazio.")

    qs = doc.questions
    ids = {}
    for q in qs:
        if q.qid in ids:
            rep.add("ERRO", q.label, f"ID duplicado (também na linha {ids[q.qid]}).")
        else:
            ids[q.qid] = q.line
    pos = {q.qid: q.index for q in qs}
    letter_ids = {q.qid for q in qs if re.fullmatch(r"[A-L]", q.qid)}
    cotas_text = " ".join(" ".join(t.header + sum(t.rows, [])) for s in doc.sections if s.kind == "cotas" for t in s.tables)
    for L in re.findall(r"\b([A-L])\.\s", cotas_text):
        letter_ids.add(L)

    # ---------- códigos das perguntas (inclui tabelas combinadas)
    codes: dict[str, list[dict]] = {q.qid: [] for q in qs}
    for q in qs:
        for t in q.tables:
            cols = combined_columns(t)
            if cols:
                for r in t.rows:
                    r = r + [""] * (len(t.header) - len(r))
                    for ci, cq in cols:
                        if cq in codes:
                            codes[cq].append({"label": r[0], "code": r[ci].strip(), "action": None})
            else:
                codes[q.qid].extend(option_rows(t))

    # ---------- varre linhas de cada pergunta
    for q in qs:
        all_lines = [(q.line, q.text, "enunciado")] + [(l, s, "pre") for l, s in q.pre_lines] + \
                    [(l, s, "corpo") for l, s in q.body_lines]
        for t in q.tables:
            for r in t.rows:
                all_lines.append((t.line, " | ".join(r), "tabela"))

        for ln, s, kind in all_lines:
            where = f"{q.label} (linha {ln})"
            # referências inexistentes
            for ref in refs_in(s):
                if ref not in pos:
                    rep.add("ERRO", where, f"Referência a P.{ref}, que não existe no questionário.")
            for m in LETTER_REF_RE.finditer(s):
                if m.group(1) not in letter_ids:
                    rep.add("ALERTA", where, f"Referência a P.{m.group(1)} (controle de cotas) sem pergunta/cota correspondente.")
            # pulos
            skip_targets = set()
            for m in SKIP_RE.finditer(s):
                tgt = m.group(3).upper()
                skip_targets.add(tgt)
                if tgt in pos and pos[tgt] <= q.index and kind != "pre":
                    rep.add("ERRO", where, f"Pulo para P.{tgt} não avança (pulo para trás ou para a própria pergunta).")
                if tgt in pos and kind == "pre" and pos[tgt] < q.index:
                    rep.add("ERRO", where, f"Pulo para P.{tgt}, anterior a esta posição.")
            # referências para frente fora de contexto de pulo/aplicação
            if kind in ("enunciado", "corpo", "pre") and not FORWARD_OK_RE.search(s):
                for ref in refs_in(s):
                    if ref in pos and pos[ref] > q.index and ref not in skip_targets:
                        rep.add("ALERTA", where, f"Menção a P.{ref}, posterior — pipe/filtro não pode depender de pergunta futura.")
            # placeholders
            for ph, lvl in PLACEHOLDERS:
                if ph in s.upper():
                    rep.add(lvl, where, f"Placeholder '{ph}' no texto.")
            # maiúsculas
            if kind in ("pre", "corpo") and is_instruction(s) and uppercase_violation(s.split(":", 1)[-1] if ":" in s else s):
                rep.add("ALERTA", where, "Instrução não está em MAIÚSCULAS.")

        # código de tipo de resposta
        if not is_roteiro:
            blob = q.text + " " + " ".join(s for _, s in q.pre_lines + q.body_lines)
            if not TYPE_CODE_RE.search(blob) and not re.fullmatch(r"[A-L]", q.qid):
                rep.add("ALERTA", q.label, "Sem código de tipo de resposta — (RU), (RM), (ESPONTÂNEO), (RU POR LINHA)...")

        # online / CAPI: NOVA TELA
        if modo in ("online", "capi", "clt", "hut") and not q.new_screen:
            rep.add("ALERTA", q.label, "Falta 'NOVA TELA:' antes da pergunta (modo online/CAPI).")

        # rodízio em perguntas de marca estimuladas
        tu = strip_accents(q.text.upper())
        if "MARCA" in tu and ("MOSTRAR" in tu or "LEIA" in tu or "LER " in tu or "SHOW" in tu) \
                and "RODIZ" not in tu and "RANDOMIZ" not in tu \
                and not any("RODIZ" in strip_accents(s.upper()) or "RANDOMIZ" in s.upper() for _, s in q.pre_lines + q.body_lines):
            rep.add("ALERTA", q.label, "Lista de marcas estimulada sem (RODIZIAR MARCAS).")

    # ---------- opções: roteamento na triagem, Nenhum = 99
    for q in qs:
        sec_up = strip_accents(q.section.upper())
        screening = any(w in sec_up for w in SCREEN_SECTION_WORDS)
        for t in q.tables:
            if combined_columns(t):
                continue
            opts = option_rows(t)
            for o in opts:
                lab = strip_accents(o["label"].lower())
                if re.match(r"^(nenhum|nenhuma)\b", lab) and o["code"] not in ("99", "///", "//", ""):
                    rep.add("ALERTA", q.label, f"Opção '{o['label']}' deveria ter código 99 (EXCLUSIVA).")
                if screening and o["action"] is not None and not o["action"]:
                    rep.add("ERRO", q.label, f"Opção '{o['label']}' sem roteamento (CONTINUE / ENCERRE / PULE PARA) em seção de triagem.")
            if screening and opts and all(o["action"] is None for o in opts) and not re.fullmatch(r"[A-L]", q.qid):
                if any(o["code"] for o in opts):
                    rep.add("ALERTA", q.label, "Pergunta de triagem sem coluna 'Ação' (roteamento).")

    # ---------- coerência pulo ↔ filtro de base
    for q in qs:
        for t in q.tables:
            for o in option_rows(t):
                act = o["action"] or ""
                m = SKIP_RE.search(act)
                if not m:
                    continue
                tgt = m.group(3).upper()
                if tgt not in pos:
                    continue
                for skipped in qs[q.index + 1: pos[tgt]]:
                    blob = " ".join(s for _, s in skipped.pre_lines + skipped.body_lines) + " " + skipped.text
                    if not re.search(rf"[PQ]\.?\s?{re.escape(q.qid)}(?![\dA-Za-z])", blob, re.IGNORECASE):
                        rep.add("ALERTA", skipped.label,
                                f"É pulada por quem responde '{o['label']}' em {q.label}, mas não tem filtro de base "
                                f"(ex.: 'SOMENTE PARA CÓD ... NA {q.label}').")

    # ---------- escalas
    for q in qs:
        for t in q.tables:
            cands: list[list[str]] = []
            opts = option_rows(t)
            if 4 <= len(opts) <= 11:
                cands.append([norm_label(o["label"]) for o in opts])
            if len(t.header) >= 6:
                cands.append([norm_label(h) for h in t.header[1:] if h.strip()])
            for labels in cands:
                best, best_hit = None, 0
                for name, std in STD_SCALES.items():
                    hit = sum(1 for lab in labels if lab in std)
                    if hit > best_hit:
                        best, best_hit = name, hit
                if best and best_hit >= 3 and (best_hit < 5 or len(labels) != 5):
                    rep.add("ALERTA", q.label, f"Escala parecida com '{best}', mas diferente do padrão okno: "
                            f"{' / '.join(STD_SCALES[best])}.")

    # ---------- blocos obrigatórios
    full = "\n".join(doc.lines).upper()
    full_na = strip_accents(full)
    if tipo in QUANTI_TYPES_WITH_SCREENER:
        required = {
            "Critério Brasil": "CRITERIO BRASIL" in full_na,
            "Sexo": "SEXO" in full_na or "GENDER" in full_na or "IDENTIFICA COMO" in full_na,
            "Idade": "IDADE" in full_na or "HOW OLD" in full_na,
            "Filtro de área de atuação": "TRABALHA EM" in full_na or "WORK IN" in full_na,
        }
        for k, ok in required.items():
            if not ok:
                rep.add("ERRO", "triagem", f"Bloco fixo ausente: {k}.")
    if not is_roteiro and not any(s.kind == "encerramento" for s in doc.sections):
        rep.add("ERRO", "encerramento", "Seção '## ENCERRAMENTO' ausente.")

    # ---------- tamanho das seções
    per_sec: dict[str, int] = {}
    for q in qs:
        per_sec[q.section] = per_sec.get(q.section, 0) + 1
    for sec, n in per_sec.items():
        if n > 30:
            rep.add("ALERTA", sec, f"Seção com {n} perguntas (> 30 exige aprovação).")

    # ---------- pendências
    n_prop = full.count("[PROPOSTO PELA IA")
    if n_prop:
        rep.add("INFO", "geral", f"{n_prop} trecho(s) marcados [PROPOSTO PELA IA — VALIDAR].")
    if not any(s.kind == "mapa" for s in doc.sections):
        rep.add("ALERTA", "geral", "Seção '## MAPA DE COBERTURA' ausente (objetivo → perguntas).")

    rep.add("INFO", "geral", f"{len(qs)} perguntas; {len(doc.sections)} seções; tipo={tipo or '?'}; modo={modo or '?'}.")
    return rep


def render(rep: Report, path: str) -> str:
    out = [f"# Checagem automática — {path}", "",
           f"**ERRO:** {rep.count('ERRO')} · **ALERTA:** {rep.count('ALERTA')} · **INFO:** {rep.count('INFO')}", ""]
    for lvl in ("ERRO", "ALERTA", "INFO"):
        items = [i for i in rep.items if i["nivel"] == lvl]
        if not items:
            continue
        out.append(f"## {lvl}")
        seen = set()
        for i in items:
            key = (i["onde"], i["msg"])
            if key in seen:
                continue
            seen.add(key)
            out.append(f"- **{i['onde']}** — {i['msg']}")
        out.append("")
    return "\n".join(out)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    doc = parse(path)
    rep = check(doc)
    if "--json" in sys.argv:
        print(json.dumps(rep.items, ensure_ascii=False, indent=2))
    else:
        print(render(rep, path))
    return 1 if rep.count("ERRO") else 0


if __name__ == "__main__":
    sys.exit(main())
