# questgenerator — gerador de questionários okno

Este repositório é um **sistema em loop para gerar questionários da okno Núcleo de Estudos** com Claude Code.
Converse em **PT-BR**.

## Quando o usuário pedir um questionário, roteiro, recrutamento, pré-tarefa ou diário
Carregue a skill **`okno-questionario`** e siga o loop dela (descoberta → lacunas → tipo/módulos → construção →
revisão do analista sênior → correção → exportação .docx). Não escreva perguntas sem antes carregar
**`okno-linguagem`** e o modelo do tipo em **`okno-modelos`**. Esta regra vale sobre qualquer outra skill genérica de
questionário disponível na conta: para projetos okno, use sempre as skills deste repositório.

## Mapa do repositório
| Caminho | O que é |
|---|---|
| `.claude/skills/okno-questionario/` | Orquestrador do loop + checklist de descoberta + formato intermediário |
| `.claude/skills/okno-linguagem/` | Linguagem okno: códigos, instruções, escalas, blocos fixos, pulos, funil de marcas |
| `.claude/skills/okno-modelos/` | Modelos por metodologia (quali e quanti) e módulos Conjoint, MaxDiff, PSM |
| `.claude/skills/okno-revisao-senior/` | Protocolo de revisão (pulos, linguagem, cobertura do briefing) |
| `.claude/agents/analista-senior.md` | Subagente revisor usado na etapa 5 |
| `scripts/checar_questionario.py` | Checador determinístico (pulos, referências, placeholders, escalas, maiúsculas) |
| `scripts/gerar_docx.py` | Exporta o questionário .md para .docx no padrão visual okno |
| `scripts/extrair_texto.py` | Extrai texto de docx/pptx/xlsx/pdf da pasta de entrada |
| `scripts/empacotar_skill.py` | Gera `dist/okno-questionario.zip` para o admin subir no claude.ai (ver `empacotamento/`) |
| `projetos/<slug>/` | Um projeto por pasta: `entrada/`, ficha, versões do questionário, pareceres, .docx |
| `referencias/` | Guia de estilo e referências okno (índice do Drive) + benchmarks de mercado resumidos |

## Comandos
```bash
pip install -r requirements.txt
python3 scripts/extrair_texto.py projetos/<slug>/entrada/
python3 scripts/checar_questionario.py projetos/<slug>/<tipo>-v<N>.md
python3 scripts/gerar_docx.py projetos/<slug>/<tipo>-v<N>.md
```

## Regras
- Ao alterar qualquer skill, rode `python3 scripts/empacotar_skill.py` e confirme que não há avisos de referências não convertidas.
- Informação dos arquivos do projeto > referência okno > guia de estilo > conhecimento geral.
- Perguntas ao usuário sempre com a opção **"Não tenho essa informação"**; só então a IA cria a informação e marca
  `[PROPOSTO PELA IA — VALIDAR]`.
- Nunca commitar arquivos de `projetos/*/entrada/` (dados de cliente) — já estão no `.gitignore`.
