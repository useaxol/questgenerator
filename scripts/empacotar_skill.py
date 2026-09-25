#!/usr/bin/env python3
"""Empacota o sistema okno como UMA skill autocontida (.zip) para upload no claude.ai
(Configurações › Skills — individual ou, pelo admin, para toda a organização).

Uso:
    python3 scripts/empacotar_skill.py            # gera dist/okno-questionario.zip

A fonte de verdade continua sendo .claude/skills/ (usada pelo Claude Code). Este script copia os arquivos,
ajusta os caminhos entre eles e usa empacotamento/claude-ai/SKILL.md como ponto de entrada.
"""
from __future__ import annotations

import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"
DIST = ROOT / "dist"
NAME = "okno-questionario"

# (origem, destino relativo dentro da skill)
FILES: list[tuple[Path, str]] = [
    (ROOT / "empacotamento/claude-ai/SKILL.md", "SKILL.md"),
    (SKILLS / "okno-linguagem/SKILL.md", "LINGUAGEM.md"),
    (SKILLS / "okno-modelos/SKILL.md", "MODELOS.md"),
    (SKILLS / "okno-revisao-senior/SKILL.md", "REVISAO.md"),
    (ROOT / ".claude/agents/analista-senior.md", "ANALISTA-SENIOR.md"),
    (SKILLS / "okno-questionario/references/checklist-descoberta.md", "orquestracao/checklist-descoberta.md"),
    (SKILLS / "okno-questionario/references/formato-markdown.md", "orquestracao/formato-markdown.md"),
    (ROOT / "referencias/README.md", "referencias/README.md"),
]
DIRS: list[tuple[Path, str]] = [
    (SKILLS / "okno-linguagem/references", "linguagem"),
    (SKILLS / "okno-modelos/modelos", "modelos"),
    (SKILLS / "okno-modelos/modulos", "modulos"),
    (ROOT / "referencias/benchmarks", "referencias/benchmarks"),
]
SCRIPTS = ["okno_md.py", "checar_questionario.py", "gerar_docx.py", "extrair_texto.py"]

# Reescrita de caminhos/nomes: a ordem importa (específico → genérico).
REWRITES: list[tuple[str, str]] = [
    ("okno-linguagem/references/", "linguagem/"),
    ("okno-questionario/references/", "orquestracao/"),
    ("okno-modelos/modelos/", "modelos/"),
    ("okno-modelos/modulos/", "modulos/"),
    ("`okno-linguagem`", "`LINGUAGEM.md`"),
    ("`okno-modelos`", "`MODELOS.md`"),
    ("`okno-revisao-senior`", "`REVISAO.md`"),
    ("`okno-questionario`", "`SKILL.md`"),
    ("okno-linguagem", "LINGUAGEM.md"),
    ("okno-modelos", "MODELOS.md"),
    ("okno-revisao-senior", "REVISAO.md"),
    ("projetos/<slug-do-projeto>/", ""),
    ("projetos/<slug>/", ""),
    ("na raiz do repositório", "nesta skill"),
]
# Reescritas só dentro de LINGUAGEM.md (caminhos relativos ao antigo diretório da skill)
LINGUAGEM_REWRITES = [("`references/", "`linguagem/")]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def transform(text: str, dest: str) -> str:
    if dest != "SKILL.md":
        text = strip_frontmatter(text)
    if dest == "LINGUAGEM.md":
        for a, b in LINGUAGEM_REWRITES:
            text = text.replace(a, b)
    if dest != "SKILL.md":
        for a, b in REWRITES:
            text = text.replace(a, b)
    if dest == "ANALISTA-SENIOR.md":
        text = text.replace("Carregue a skill `REVISAO.md`", "Leia `REVISAO.md`")
        text = text.replace("Carregue também `LINGUAGEM.md`", "Leia também `LINGUAGEM.md`")
        text = text.replace("`references/", "`linguagem/")
        text = text.replace("`scripts/checar_questionario.py", "`<pasta-da-skill>/scripts/checar_questionario.py")
    return text


def build() -> Path:
    out = DIST / NAME
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    for src, dest in FILES:
        target = out / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(transform(src.read_text(encoding="utf-8"), dest), encoding="utf-8")
    for src_dir, dest_dir in DIRS:
        for src in sorted(src_dir.glob("*.md")):
            dest = f"{dest_dir}/{src.name}"
            target = out / dest
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(transform(src.read_text(encoding="utf-8"), dest), encoding="utf-8")
    (out / "scripts").mkdir()
    for s in SCRIPTS:
        shutil.copy2(ROOT / "scripts" / s, out / "scripts" / s)
    shutil.copy2(ROOT / "requirements.txt", out / "scripts" / "requirements.txt")

    # checagem: nenhuma referência às pastas do repositório deve sobrar
    leftovers = []
    for f in out.rglob("*.md"):
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if re.search(r"\.claude/|okno-(linguagem|modelos|revisao-senior)|projetos/|`references/", line):
                leftovers.append(f"{f.relative_to(out)}:{n}: {line.strip()[:100]}")
    if leftovers:
        print("ATENÇÃO — referências não convertidas:\n  " + "\n  ".join(leftovers))

    zpath = DIST / f"{NAME}.zip"
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(out.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                z.write(f, f"{NAME}/{f.relative_to(out)}")
    return zpath


def main() -> int:
    z = build()
    with zipfile.ZipFile(z) as zf:
        n = len(zf.namelist())
    print(f"OK: {z} ({n} arquivos, {z.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
