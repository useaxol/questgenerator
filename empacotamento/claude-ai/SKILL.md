---
name: okno-questionario
description: Gera questionários da okno Núcleo de Estudos (quali e quanti) em loop — lê os arquivos do projeto (briefing, proposta, questionários anteriores), pergunta o que falta sempre com a opção "Não tenho essa informação", define o tipo (recrutamento, pré-tarefa, roteiro de discussão, ad hoc, teste de produto, embalagem, comunicação, tracking de marca, diário de uso) e módulos (Conjoint, MaxDiff, PSM), redige na linguagem okno, passa por revisão de analista sênior (pulos, linguagem, cobertura do briefing) até aprovação e entrega o .docx no padrão okno. Use sempre que alguém pedir para criar, montar, revisar ou corrigir um questionário, roteiro, filtro/recrutamento, pré-tarefa ou diário de uso da okno.
---

# Gerador de questionários okno — o loop

Esta skill é autocontida. Todos os caminhos abaixo são **relativos à pasta desta skill** (onde está este SKILL.md).

| Arquivo / pasta | Conteúdo | Quando ler |
|---|---|---|
| `LINGUAGEM.md` + `linguagem/` | Linguagem okno: códigos, instruções, escalas, blocos fixos, Critério Brasil, pulos, funil de marcas | **Sempre**, antes de escrever qualquer pergunta |
| `MODELOS.md` + `modelos/` + `modulos/` | Modelo de cada metodologia e módulos Conjoint, MaxDiff, PSM | Etapa 4, o modelo do tipo escolhido |
| `REVISAO.md` + `ANALISTA-SENIOR.md` | Protocolo e papel do analista sênior | Etapa 5 |
| `orquestracao/checklist-descoberta.md` | Ficha do projeto e perguntas-modelo | Etapas 1–3 |
| `orquestracao/formato-markdown.md` | Formato intermediário do questionário | Etapa 4 |
| `scripts/` | `checar_questionario.py`, `gerar_docx.py`, `extrair_texto.py` | Etapas 1, 4, 6, 7 |
| `referencias/` | Índice das referências okno e benchmarks de mercado | Quando o tipo não tiver modelo okno |

**Ambiente**: os scripts rodam na ferramenta de execução de código (Python). Na primeira execução, instale as
dependências se faltarem: `pip install python-docx python-pptx openpyxl pypdf`. Chame os scripts pelo caminho
completo da skill, ex.: `python3 <pasta-da-skill>/scripts/checar_questionario.py questionario-v1.md`.
Trabalhe numa pasta de trabalho da conversa e salve os entregáveis finais na pasta de saída/arquivos para download.

Nunca invente informação que exista nos arquivos do projeto. Toda informação criada pela IA é marcada
`[PROPOSTO PELA IA — VALIDAR]`. Converse em PT-BR, de forma breve, dizendo em que etapa está.

```
1 DESCOBERTA → 2 LACUNAS → 3 TIPO + MÓDULOS → 4 CONSTRUÇÃO → 5 REVISÃO SÊNIOR ⇄ 6 CORREÇÃO → 7 .docx → 8 PRÓXIMO?
```

## ETAPA 1 — DESCOBERTA (ler antes de perguntar)
1. Leia **todos** os arquivos anexados na conversa e os do Projeto (Claude Projects), se houver. Para docx/pptx/xlsx/pdf
   use `scripts/extrair_texto.py <arquivo>`.
2. Se houver conector de Google Drive / OneDrive / SharePoint / Notion e o usuário indicar uma pasta, busque lá também
   (briefing, proposta, questionário anterior do mesmo cliente/JOB).
3. Preencha a ficha de `orquestracao/checklist-descoberta.md` registrando a **fonte** de cada campo (arquivo + trecho)
   ou `NÃO ENCONTRADO`. Salve como `ficha-projeto.md`.
4. Mostre um resumo curto: o que achou (com fonte) e o que falta.

## ETAPA 2 — LACUNAS
Para cada campo essencial `NÃO ENCONTRADO`, pergunte ao usuário — com a ferramenta de perguntas de múltipla escolha,
se disponível; senão, em uma mensagem com opções numeradas. Regras:
- **Toda pergunta inclui a opção `Não tenho essa informação`** (sempre a última).
- Ofereça 2–3 opções plausíveis baseadas no que já foi lido. Agrupe por tema (máx. 4 perguntas por vez).
- Só quando a resposta for `Não tenho essa informação`, crie a informação com base no que estiver disponível e registre
  na ficha como `[PROPOSTO PELA IA — VALIDAR]` + justificativa de uma linha.
- Não pergunte o que já está nos arquivos.

## ETAPA 3 — TIPO + MÓDULOS
Se o tipo não estiver explícito, pergunte (com `Não tenho essa informação`; nesse caso recomende). Tipos e modelos em
`MODELOS.md`: recrutamento quali, pré-tarefa, roteiro de discussão, ad hoc, teste de produto (recrutamento + principal),
teste de embalagem, teste de comunicação, tracking de marca, diário de uso. Módulos quanti: Conjoint, MaxDiff, PSM —
cada um exige insumos próprios (volte à etapa 2 só para eles se faltarem). Liste os documentos do projeto (ex.:
recrutamento + principal) e confirme a ordem. Feche e mostre a ficha — ela é o contrato da construção.

## ETAPA 4 — CONSTRUÇÃO
1. Leia `LINGUAGEM.md` (e as referências em `linguagem/` que o tipo exige) e o modelo do tipo em `modelos/` / `modulos/`.
2. Escreva o questionário em `<tipo>-v1.md` no formato de `orquestracao/formato-markdown.md`.
3. Inclua no fim a seção `## MAPA DE COBERTURA` (objetivo do briefing → perguntas → KPI).
4. Rode `scripts/checar_questionario.py <tipo>-v1.md` e corrija todo ERRO antes da revisão.

## ETAPA 5 — REVISÃO PELO ANALISTA SÊNIOR
Se houver ferramenta de subagente/tarefa, delegue a revisão a um subagente com as instruções de `ANALISTA-SENIOR.md`.
Se não houver, faça a revisão **numa passada separada**: releia o questionário do zero assumindo o papel descrito em
`ANALISTA-SENIOR.md`, seguindo `REVISAO.md` à risca — (1) consistência de pulos, (2) linguagem okno, (3) cobertura do
briefing — e grave `revisao-v<N>.md` com veredito `APROVADO` / `APROVADO COM RESSALVAS` / `REPROVADO`.
Seja tão rigoroso quanto seria com o questionário de outra pessoa.

## ETAPA 6 — CORREÇÃO (loop)
Aplique todas as correções ALTA e MÉDIA (e BAIXA triviais) em `<tipo>-v<N+1>.md`; o que depender do cliente, pergunte
(com `Não tenho essa informação`). Rode o checador e volte à etapa 5. Pare quando o veredito for `APROVADO`, ou
`APROVADO COM RESSALVAS` sem ALTA/MÉDIA pendente, ou após **3 rodadas** (entregue com as pendências explícitas).

## ETAPA 7 — EXPORTAÇÃO
`scripts/gerar_docx.py <tipo>-v<N>.md` gera o `.docx` no padrão okno. Entregue para download: o `.docx`, o último
parecer do analista e a lista de pendências `[PROPOSTO PELA IA — VALIDAR]`.

## ETAPA 8 — PRÓXIMO DOCUMENTO
Pergunte se há outro documento do mesmo projeto; se sim, volte à etapa 3 reaproveitando a ficha.

## Regras de ouro
- Informação do projeto > referência okno > guia de estilo > conhecimento geral da IA.
- Nunca revelar o cliente na introdução do questionário.
- Nunca entregar com placeholders (`CONTINUAR OU ENCERRAR`, `[INSERIR…]`, `MARCA 1…N` sem pipe).
