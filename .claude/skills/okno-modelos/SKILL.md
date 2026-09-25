---
name: okno-modelos
description: Modelos estruturais okno por metodologia — recrutamento quali, pré-tarefa, roteiro de discussão, ad hoc, teste de produto (recrutamento e principal), teste de embalagem, teste de comunicação, tracking de marca, diário de uso — e módulos Conjoint, MaxDiff e PSM. Use junto com okno-linguagem ao construir qualquer questionário okno, para seguir a sequência de blocos e as perguntas-padrão de cada metodologia.
---

# Modelos okno por metodologia

Cada modelo traz: **sequência de blocos**, **perguntas-padrão (texto literal okno)**, **lógica de pulos típica**
e **como cada bloco responde a objetivos comuns de briefing**. Use o modelo como esqueleto e personalize com a
ficha do projeto. A redação segue sempre `okno-linguagem`.

| Tipo | Arquivo | Referência real |
|---|---|---|
| Recrutamento quali (GD/EP) | `modelos/quali-recrutamento.md` | padrão recrutamento Inco + boas práticas |
| Pré-tarefa | `modelos/quali-pre-tarefa.md` | — |
| Roteiro de discussão | `modelos/quali-roteiro-discussao.md` | — |
| Ad hoc (U&A, imagem, segmentação) | `modelos/quanti-adhoc.md` | Guia §7 + benchmark Segmentação |
| Teste de produto | `modelos/quanti-teste-produto.md` | Inco 88.24.010 (recrutamento + principal) |
| Teste de embalagem | `modelos/quanti-teste-embalagem.md` | Inco (bloco embalagem) + benchmark Pack |
| Teste de comunicação | `modelos/quanti-teste-comunicacao.md` | Guia §7.5 |
| Tracking de marca | `modelos/quanti-tracking-marca.md` | Cachaça 183.25.002 + Varejo 267.25.006 |
| Diário de uso | `modelos/diario-de-uso.md` | Inco (diário de pesagem) |
| Conjoint | `modulos/conjoint.md` | benchmark Conjoint |
| MaxDiff | `modulos/maxdiff.md` | — |
| PSM | `modulos/psm.md` | Inco P.64A–D |

Benchmarks de mercado resumidos (estrutura, não linguagem): `referencias/benchmarks/*.md` na raiz do repositório.
Quando um benchmark e o padrão okno divergirem (ex.: escala de 7 pontos no benchmark), **vale o padrão okno**.

## Regras comuns a todos os modelos quanti

1. Triagem com blocos fixos (Critério Brasil → Sexo → Idade → Área de atuação) + filtros de categoria.
2. Do geral para o específico: hábitos da categoria → marcas → estímulo → diagnóstico → comparação → preço → perfil.
3. Avaliação global (gostar, intenção) **antes** dos atributos, para não contaminar.
4. Abertas de gostou/não gostou logo depois da avaliação global.
5. Módulos (PSM, MaxDiff, Conjoint) depois da avaliação do estímulo e antes do perfil final.
6. Todo KPI de action standard do briefing precisa de uma pergunta fechada correspondente.
