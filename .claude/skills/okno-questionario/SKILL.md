---
name: okno-questionario
description: Sistema em loop para gerar questionários okno (quali e quanti) a partir dos arquivos do projeto — descoberta no briefing, perguntas ao usuário com opção "Não tenho essa informação", escolha do tipo (recrutamento, pré-tarefa, roteiro, ad hoc, teste de produto/embalagem/comunicação, tracking, diário de uso) e módulos (Conjoint, MaxDiff, PSM), redação na linguagem okno, revisão por analista sênior e correção até aprovação, com exportação em .docx. Use quando o usuário pedir para criar, gerar, montar ou revisar um questionário, roteiro ou recrutamento.
---

# Gerador de questionários okno — o loop

Você conduz o usuário por um **loop de 6 etapas**. Nunca pule etapas e nunca invente informação que exista nos
arquivos do projeto. Toda informação criada pela IA é marcada `[PROPOSTO PELA IA — VALIDAR]`.

```
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ 1 DESCOBERTA → 2 LACUNAS (perguntar) → 3 TIPO + MÓDULOS → 4 CONSTRUÇÃO   │
 │        ▲                                                   │             │
 │        │                                                   ▼             │
 │   8 PRÓXIMO QUESTIONÁRIO?  ←  7 EXPORTAR .docx  ←  5 REVISÃO SÊNIOR ⇄ 6 CORREÇÃO │
 └──────────────────────────────────────────────────────────────────────────┘
```

Pasta de trabalho de cada projeto: `projetos/<slug-do-projeto>/`
- `entrada/` — arquivos que o usuário forneceu (briefing, proposta, e-mails, questionários anteriores, listas de marcas)
- `ficha-projeto.md` — ficha consolidada (etapas 1–3)
- `<tipo>-v<N>.md` — questionário no formato intermediário (etapa 4)
- `revisao-v<N>.md` — parecer do analista sênior (etapa 5)
- `<tipo>-v<N>.docx` — entrega final (etapa 7)

Crie a pasta se não existir. Se o usuário anexou arquivos na conversa ou colou texto, salve-os em `entrada/`.

---

## ETAPA 1 — DESCOBERTA (ler antes de perguntar)

1. Liste e leia **todos** os arquivos de `projetos/<slug>/entrada/` (docx → use a skill de docx ou
   `python3 scripts/extrair_texto.py <arquivo>`; pdf, pptx, xlsx, md, txt, e-mails).
2. Se houver conector do Google Drive / OneDrive / Notion disponível **e** o usuário indicou uma pasta, busque lá
   também (briefing, proposta, questionário anterior do mesmo cliente/JOB).
3. Preencha a ficha usando `references/checklist-descoberta.md`. Para cada campo registre a **fonte**
   (arquivo + trecho) ou `NÃO ENCONTRADO`.
4. Mostre ao usuário um resumo curto: o que achou (com fonte) e o que falta.

## ETAPA 2 — LACUNAS (perguntar ao usuário)

Para cada campo essencial `NÃO ENCONTRADO`, pergunte usando a ferramenta **AskUserQuestion** (máx. 4 perguntas por
chamada; agrupe por tema). Regras:

- **Toda pergunta inclui a opção `Não tenho essa informação`** (sempre como última opção listada).
- Ofereça 2–3 opções plausíveis baseadas no que já foi lido (ex.: faixas etárias do público citado na proposta).
- Só quando a resposta for `Não tenho essa informação`, **a IA cria a informação** com base em qualquer dado
  disponível (categoria, público, objetivo, questionários de referência, conhecimento de mercado) e registra na
  ficha como `[PROPOSTO PELA IA — VALIDAR]` + a justificativa em uma linha.
- Não pergunte o que já está nos arquivos. Não pergunte campos opcionais se o essencial já permite construir.

## ETAPA 3 — TIPO DE QUESTIONÁRIO + MÓDULOS

Se o tipo não estiver explícito no briefing, pergunte (AskUserQuestion, com `Não tenho essa informação`; nesse
caso recomende o tipo com base no objetivo). Tipos:

| Grupo | Tipo | Modelo |
|---|---|---|
| Qualitativo | Questionário de recrutamento (filtro) | `okno-modelos` → `modelos/quali-recrutamento.md` |
| Qualitativo | Pré-tarefa (GD / EP) | `modelos/quali-pre-tarefa.md` |
| Qualitativo | Roteiro de discussão | `modelos/quali-roteiro-discussao.md` |
| Quantitativo | Projeto ad hoc (U&A, hábitos, imagem, segmentação) | `modelos/quanti-adhoc.md` |
| Quantitativo | Teste de produto (CLT/HUT; recrutamento + principal) | `modelos/quanti-teste-produto.md` |
| Quantitativo | Teste de embalagem | `modelos/quanti-teste-embalagem.md` |
| Quantitativo | Teste de comunicação (pré/pós) | `modelos/quanti-teste-comunicacao.md` |
| Quantitativo | Tracking de marca | `modelos/quanti-tracking-marca.md` |
| Quanti/Quali | Diário de uso | `modelos/diario-de-uso.md` |

Módulos adicionais (só quanti; pergunte **multiSelect** se o briefing não disser): Conjoint (`modulos/conjoint.md`),
MaxDiff (`modulos/maxdiff.md`), PSM / Van Westendorp (`modulos/psm.md`). Cada módulo exige insumos próprios
(atributos e níveis; lista de itens; escada de preços) — se faltarem, volte à ETAPA 2 só para eles.

Um mesmo projeto pode precisar de mais de um documento (ex.: teste de produto = recrutamento + principal; quali =
recrutamento + pré-tarefa + roteiro). Liste-os e confirme a ordem de produção com o usuário.

Feche a ficha (`ficha-projeto.md`) e mostre-a. Ela é o contrato para a construção.

## ETAPA 4 — CONSTRUÇÃO

1. Carregue a skill **`okno-linguagem`** (obrigatório) e o modelo do tipo em **`okno-modelos`**.
2. Se existir referência okno do mesmo tipo em `referencias/` ou no Drive (mapa no Guia de Estilo §12), use-a como
   espelho de estrutura.
3. Escreva o questionário em `projetos/<slug>/<tipo>-v1.md` no **formato intermediário**
   (`references/formato-markdown.md`) — ele é lido pelo checador e pelo gerador de .docx.
4. Construa um **mapa de cobertura**: cada objetivo/área de abordagem do briefing → perguntas que o respondem.
   Escreva-o no fim do arquivo na seção `## MAPA DE COBERTURA` (não vai para o .docx).
5. Rode o checador determinístico e corrija tudo que for ERRO antes de chamar o analista:
   `python3 scripts/checar_questionario.py projetos/<slug>/<tipo>-v1.md`

## ETAPA 5 — REVISÃO PELO ANALISTA SÊNIOR

Chame o subagente **`analista-senior`** (ferramenta Agent, `subagent_type: analista-senior`) passando os caminhos da
ficha, do questionário e do relatório do checador. Ele avalia, com a skill `okno-revisao-senior`:

1. **Consistência dos pulos** (filtros, pipes, transferências, cotas, caminhos órfãos);
2. **Coerência com a linguagem okno** (skill `okno-linguagem`);
3. **Cobertura do briefing** (cada área de abordagem respondida por ≥1 pergunta adequada; nada supérfluo).

Ele grava `projetos/<slug>/revisao-v<N>.md` com veredito `APROVADO`, `APROVADO COM RESSALVAS` ou `REPROVADO` e a
lista de apontamentos (id, severidade, pergunta, problema, correção sugerida).

## ETAPA 6 — CORREÇÃO (loop)

- Aplique **todas** as correções de severidade ALTA e MÉDIA; BAIXA quando for trivial. Gere `<tipo>-v<N+1>.md`.
- Se um apontamento depende de decisão do cliente, pergunte ao usuário (com `Não tenho essa informação`).
- Rode o checador de novo e volte à ETAPA 5.
- **Pare o loop** quando o veredito for `APROVADO` (ou `APROVADO COM RESSALVAS` sem pendência ALTA/MÉDIA), ou após
  **3 rodadas** — nesse caso, entregue com a lista de pendências explícita para decisão humana.

## ETAPA 7 — EXPORTAÇÃO

`python3 scripts/gerar_docx.py projetos/<slug>/<tipo>-v<N>.md` → gera `<tipo>-v<N>.docx` no padrão visual okno
(cabeçalho, tabela de controle, títulos em caixa teal, instruções em maiúsculas coloridas, tabelas de códigos,
rodapé). Entregue ao usuário: o .docx, o parecer final do analista e as pendências `[PROPOSTO PELA IA — VALIDAR]`.

## ETAPA 8 — PRÓXIMO QUESTIONÁRIO

Pergunte se há outro documento do mesmo projeto (ex.: depois do recrutamento, o principal). Se sim, volte à ETAPA 3
reaproveitando a ficha (não refaça a descoberta).

---

## Regras de ouro

- **Informação do projeto > referência okno > guia de estilo > conhecimento geral da IA**, nesta ordem.
- Nunca revele o cliente na introdução do questionário.
- Nunca deixe placeholders (`CONTINUAR OU ENCERRAR`, `[INSERIR…]`) na versão entregue; se não houver dado, use
  `[PROPOSTO PELA IA — VALIDAR]` com a proposta concreta.
- Comunique-se com o usuário em PT-BR, de forma breve: diga em qual etapa está e o que vem a seguir.
