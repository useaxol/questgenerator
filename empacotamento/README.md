# Distribuição para a okno (claude.ai)

O repositório tem duas formas de uso:

| Onde | Como | Para quem |
|---|---|---|
| **Claude Code** (este repositório) | As skills em `.claude/skills/` carregam sozinhas | Quem mantém e evolui o sistema |
| **claude.ai / app Claude** (conta da okno) | Skill única `okno-questionario.zip`, enviada pelo admin | Toda a equipe da okno |

## 1. Gerar o arquivo para download

```bash
python3 scripts/empacotar_skill.py
```

Resultado: `dist/okno-questionario.zip` (~110 KB). Ele contém uma skill **autocontida**:

```
okno-questionario/
├── SKILL.md                 ← ponto de entrada (loop adaptado ao claude.ai)
├── LINGUAGEM.md + linguagem/     ← linguagem okno
├── MODELOS.md + modelos/ + modulos/  ← metodologias e Conjoint/MaxDiff/PSM
├── REVISAO.md + ANALISTA-SENIOR.md   ← revisão sênior
├── orquestracao/            ← ficha de descoberta e formato intermediário
├── referencias/             ← índice okno + benchmarks
└── scripts/                 ← checador, gerador de .docx, extrator de texto
```

O conteúdo vem de `.claude/skills/` (fonte única de verdade). **Sempre que mudar uma skill, gere o zip de novo** e
peça ao admin para substituir a versão publicada.

## 2. O que o admin faz

1. Confirmar que a organização tem **Skills** e **execução de código / criação de arquivos** habilitadas nas
   configurações de administração (os scripts de checagem e de .docx dependem disso).
2. Em Configurações → Skills (ou Capabilities), **enviar o `okno-questionario.zip`** e disponibilizá-lo para toda a
   organização. Os nomes dos menus mudam com as versões do produto; se não achar, consulte a central de ajuda da
   Anthropic sobre "skills da organização".
3. Recomendado: **desativar** para a equipe outras skills genéricas de questionário (ex.: `gerador-questionario`),
   para que o Claude não escolha a skill errada.

## 3. Como a equipe usa

Numa conversa (de preferência dentro de um **Projeto** por cliente/estudo, com o briefing e a proposta anexados):

> Crie o questionário de recrutamento deste estudo.

A skill é acionada sozinha pelo pedido. Ela lê os anexos, pergunta o que faltar (sempre com
"Não tenho essa informação"), constrói, revisa como analista sênior, corrige e entrega o `.docx` para download.

## 4. Diferenças em relação ao Claude Code

| | Claude Code | claude.ai |
|---|---|---|
| Revisão sênior | Subagente independente (`analista-senior`) | Subagente se disponível; senão, passada separada assumindo o papel |
| Arquivos do projeto | `projetos/<slug>/entrada/` | Anexos da conversa / Projeto / conectores (Drive, SharePoint) |
| Histórico de versões | Pasta do projeto no git | Arquivos da conversa (baixar v final + parecer) |
| Perguntas de lacuna | Ferramenta de múltipla escolha | Ferramenta de perguntas, se houver; senão, opções numeradas |
