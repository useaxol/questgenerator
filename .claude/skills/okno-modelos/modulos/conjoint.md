# Módulo — Conjoint (Choice-Based Conjoint / DCM)

Referência de estrutura: benchmark Kantar (`referencias/benchmarks/conjoint.md`) — exercício de escolha precedido de
bloco de marca/preço, com opção "nenhum", introdução com situação de compra real, e desenho experimental entregue
em planilha à parte. Linguagem e escalas okno.

## Insumos (ficha) — sem eles não construa o módulo
- **Atributos e níveis** (3–7 atributos; 2–6 níveis cada; preço quase sempre um atributo). Níveis mutuamente
  exclusivos, concretos, com mesmo grau de detalhe.
- **Proibições** (combinações impossíveis) e **condicionais** (ex.: preço por tamanho).
- **Tarefas por respondente**: 8–12 (+ 1–2 holdout fixas, opcional).
- **Conceitos por tela**: 3–4 + **opção "Nenhum destes"** (padrão) ou dual-response none.
- Versões de desenho: 300+ (gerado no software). `PROGRAMAÇÃO: O PLANO DE NÍVEIS/DESENHO É ENTREGUE SEPARADAMENTE EM PLANILHA`.
- Tamanho de amostra: ≥ 300 por segmento de análise (regra: n·t·a/c ≥ 500).
- Se `Não tenho essa informação` para atributos/níveis: a IA propõe a partir do briefing, concorrentes e categoria,
  marcando `[PROPOSTO PELA IA — VALIDAR]`, e o revisor sinaliza como pendência ALTA para validação do cliente.

## Posição
Depois de hábitos e marcas (dá contexto e permite cruzar por usuário de marca), antes do perfil. Nunca depois de
perguntas que mostrem preços específicos dos produtos testados.

## Pré-exercício (recomendado)
- Última compra: marca, preço pago, local ("Pense na última vez que você comprou ____").
- Aquecimento dos atributos: "Agora vamos apresentar as características que vão aparecer a seguir" (tela com todos os
  atributos e níveis explicados, sem avaliação).

## Texto
**Introdução** (NOVA TELA):
"A seguir, vamos mostrar algumas situações de compra de ____ (UNIDADE DE COMPRA). Em cada tela você verá ____ (c)
opções que diferem em ____ (LISTA DE ATRIBUTOS). Imagine que você está realmente comprando, com o seu próprio
dinheiro, no local onde costuma comprar. Escolha a opção que você compraria. Se nenhuma delas te interessar, escolha
'Nenhuma destas'. Pense como na sua última compra. Serão ____ (t) telas."

**Tarefa (repetir t vezes)**:
"Se estas fossem as únicas opções disponíveis, qual delas você compraria? (RU) (PROGRAMAÇÃO: TAREFA __ DE t –
CONCEITOS CONFORME DESENHO EXPERIMENTAL; ORDEM DOS ATRIBUTOS FIXA ENTRE TELAS E ALEATÓRIA ENTRE RESPONDENTES)"

| | Opção 1 | Opção 2 | Opção 3 | |
|---|---|---|---|---|
| Atributo A | [nível] | [nível] | [nível] | |
| Atributo B | [nível] | [nível] | [nível] | |
| Preço | R$ [nível] | R$ [nível] | R$ [nível] | |
| | ○ 1 | ○ 2 | ○ 3 | ○ Nenhuma destas 99 |

(Opcional volumétrico) "E quantas unidades você compraria desta opção? (NUMÉRICA)".

**Pós-exercício**:
- "Quais destas características foram as mais importantes para as suas escolhas? (RM, máx. 3)" (checagem de consistência).
- Aberta com pipe: "Você escolheu várias vezes ____ (MARCA/OPÇÃO MAIS ESCOLHIDA). Por quê? (ESPONTÂNEO)".

## Tabela de atributos e níveis (anexar)
| Atributo | Nível 1 | Nível 2 | Nível 3 | Nível 4 |
|---|---|---|---|---|

## Checagens do revisor
- Níveis cobrem os cenários de negócio do briefing (preço atual, preço-alvo, lançamento).
- Nenhum nível dominante óbvio sem preço correspondente; proibições documentadas.
- Unidade de compra e referência de preço iguais às do restante do questionário.
- "Nenhuma destas" presente (ou justificativa de escolha forçada).
