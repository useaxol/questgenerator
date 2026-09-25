# Funil de categoria e funil (pirâmide) de marcas — padrão okno

Sempre que houver bloco de marcas, a okno aplica um **funil filtrado**: cada nível só aceita marcas citadas no nível
anterior, com rodízio de marcas em todas as perguntas e **uma tabela única de códigos** com uma coluna por pergunta.

## 1. Funil de categoria (tipos de produto) — antes do funil de marcas

Exemplo real (Tracking Cachaça, P.7–P.13). Uma única tabela; cada coluna é uma pergunta; mesmos códigos em todas.

| Nível | Enunciado-modelo | Base / pipe | Tipo |
|---|---|---|---|
| Consumiu no último ano | "Quais destes tipos de ____ você consumiu no último ano? (MOSTRAR TABLET / LER OPÇÕES)" | Todos | (RM) |
| Consome ao menos 1x/mês | "E quais você consome pelo menos uma vez por mês? (RODIZIAR – ACEITAR SOMENTE RESPOSTAS DE P.7)" | P.7 | (RM) |
| **Filtro** | "DEVE CITAR ____ (CÓD X) EM P.8, CASO CONTRÁRIO ENCERRE" | — | — |
| Maior frequência | "Qual você consome com maior frequência? (ACEITAR SOMENTE RESPOSTAS DE P.8) (SE APENAS UMA RESPOSTA EM P.8, TRANSPORTAR PARA P.9 E VÁ PARA P.10)" | P.8 | (RU) |
| Preferida | "Qual sua ____ preferida? (ACEITAR SOMENTE RESPOSTAS DE P.7) (SE APENAS UMA RESPOSTA EM P.7, TRANSPORTAR…)" | P.7 | (RU) |
| Rejeita | "Você rejeita algum tipo de ____? (ACEITAR SOMENTE RESPOSTAS DIFERENTES DE P.8, P.9 E P.10)" | Lista − P.8/9/10 | (RM) |
| Aumentou | "Quais ____ você aumentou o consumo no último ano? (ACEITAR SOMENTE RESPOSTAS DE P.7, E DIFERENTES DE P.11)" | P.7 − P.11 | (RM) |
| Diminuiu | "E quais você diminuiu o consumo no último ano? (ACEITAR SOMENTE RESPOSTAS DIFERENTES DE P.12)" | − P.12 | (RM) |

Variante recrutamento (Inco, Q.6–Q.8): usa → usa com maior frequência → escolhe a marca e compra, com filtro
composto "PARA PARTICIPAR, DEVE CITAR CÓD 7 NA P.6, P.7 E P.8 | CASO CONTRÁRIO ENCERRE".

## 2. Pirâmide de marcas COMPLETA (brand tracking) — Guia de Estilo §8

Ordem lógica obrigatória (numere sequencialmente no questionário novo; no tracking de cachaça a numeração
P.20/P.19 aparece invertida por **compatibilidade histórica** — só mantenha numeração herdada se for onda de
tracking existente).

| # | Nível | Enunciado-modelo (literal okno) | Base / pipe | Tipo |
|---|---|---|---|---|
| 1 | Conhecimento espontâneo | "Quais marcas de ____ você conhece, mesmo que só de ouvir falar? (ESPONTÂNEO) (RM) (SE CITOU TODAS AS MARCAS, PULAR A PRÓXIMA)" | Todos | (RM) Esp. |
| 2 | Conhecimento estimulado | "E quais destas marcas de ____ você conhece, mesmo que só de ouvir falar? (MOSTRAR TABLET / LER OPÇÕES – RODIZIAR MARCAS) (RM) (APENAS PARA MARCAS NÃO CITADAS NA P.1)" | Todos, marcas não citadas | (RM) Est. |
| — | Processamento | "PROCESSAMENTO: TRANSFERIR MARCAS CITADAS NA ESPONTÂNEA PARA A ESTIMULADA" | — | — |
| — | Filtro (opcional) | "SE NÃO CONHECER NENHUMA DAS MARCAS AVALIADAS DA PRAÇA, ENCERRE" | — | — |
| 3 | Conhece pelo menos um pouco | "E quais delas você conhece pelo menos um pouco a respeito? (ACEITAR APENAS MENÇÕES DE ESP./EST.)" | 1+2 | (RM) |
| 4 | Já experimentou | "Quais você de fato já experimentou? (ACEITAR APENAS MENÇÕES DE 3)" | 3 | (RM) |
| 5 | Consumiu últimos 6 meses | "Quais delas você consumiu nos últimos 6 meses? (ACEITAR APENAS MENÇÕES DE 4)" | 4 | (RM) |
| 6 | Costuma consumir | "Quais delas você costuma consumir? (ACEITAR APENAS MENÇÕES DE 4)" | 4 | (RM) |
| 7 | Maior frequência | "Qual você consome com maior frequência? (ACEITAR APENAS MENÇÕES DE 6) (SE APENAS UMA, TRANSFERIR)" | 6 | (RU) |
| 8 | Preferida | "Qual é a sua marca de ____ preferida? (ACEITAR APENAS MENÇÕES DE 6) (SE APENAS UMA, TRANSFERIR)" | 6 | (RU) |
| 9 | Recomenda | "Quais destas marcas você costuma recomendar, sugerir aos seus amigos? (ACEITAR APENAS MENÇÕES DE 1+2) (RU) ENTREVISTADOR: SE CITAR MAIS DE UMA, PEDIR PARA SELECIONAR A QUE MAIS RECOMENDA" | 1+2 | (RU) |
| 10 | Reduziu (mas ainda consome) | "Quais dessas marcas você reduziu o consumo, mas ainda consome? (ACEITAR APENAS MENÇÕES DE 6) (SE 'NENHUMA' EM 4 OU 6, PULE PARA 11)" | 6 | (RM) |
| 11 | Consumia e parou | "Quais delas você consumia e parou de consumir? (ACEITAR APENAS MENÇÕES DE 1+2 EXCETO CITADAS EM 6) (SE EM 6 CITOU TODAS AS MARCAS DE 1+2, ASSINALAR AUTOMATICAMENTE 'NENHUMA' E VÁ PARA 12)" | (1+2) − 6 | (RM) |
| 12 | Rejeita | "Quais destas marcas você rejeita, ou seja, você não consumiria? (ACEITAR APENAS MENÇÕES DE 1+2 EXCETO CITADAS EM 6) (SE EM 6 CITOU TODAS…, ASSINALAR 'NENHUMA' E VÁ PARA 13)" | (1+2) − 6 | (RM) |
| 13 | Ruptura (opcional) | "PERGUNTAR PARA CADA MARCA CITADA EM 6 – RODIZIAR MARCAS: Quando você não encontra a marca ____ (LER MARCA), você compra outra marca de ____ ou vai até outro lugar em busca desta marca? (RU POR MARCA AVALIADA)" Compra outra = 1 · Vai a outro lugar = 2 | 6 | (RU por marca) |

`PROGRAMAÇÃO: SEMPRE RODIZIAR MARCAS EM TODAS AS PERGUNTAS DA PIRÂMIDE`

### Tabela única de códigos (formato obrigatório)

| Marca | P.16 | P.17 | P.18 | P.19 | P.20 | P.21 | P.22 | P.23 | P.24 | P.25 | P.26 | P.27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marca A | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| … | | | | | | | | | | | | |
| Outra. Especifique: | | | | | | | | | | | | |
| Nenhuma | /// | 99 | /// | /// | /// | /// | /// | /// | /// | 99 | 99 | 99 |

- `Nenhuma` = 99 **somente** nas perguntas estimuladas em que "nenhuma" é resposta válida (estimulado, reduziu,
  parou, rejeita); `///` nas demais.
- Marcas regionais: `(MOSTRAR APENAS EM <PRAÇA>)` na linha da marca.
- Códigos de marca são **estáveis entre ondas** (novas marcas recebem códigos novos, ex.: 181, 182…; nunca reaproveitar).

## 3. Pirâmide REDUZIDA (outros estudos) — Guia §8.1

Conhece estimulado → Já experimentou → Costuma consumir → Maior frequência (RU) → Preferida (RU) → Rejeita.
Mesmas regras de pipe, rodízio e transferência.

## 4. Funil de recrutamento (teste de produto) — Inco Q.19–Q.24

Conhece (RM, LER) → Já experimentou (MOSTRAR APENAS MARCAS DE Q.19) → Costuma usar (APENAS DE Q.20) →
Usa com maior frequência (RU, APENAS DE Q.21, SE SÓ 1 TRANSFERIR) → Está usando atualmente (APENAS DE Q.20) →
Rejeita (MENCIONADAS EM Q.19 E NÃO EM Q.21; SE TODAS, ASSINALAR 'NENHUMA' E PULAR).

- `NOVA TELA PARA CADA PERGUNTA DO REPERTÓRIO (RODIZIAR MARCAS – Q.19 A Q.24)`
- Coluna de filtro na tabela: marcas não-alvo com `ENCERRE` em "maior frequência"; marcas-alvo com `ENCERRE` em "rejeita".
- Filtro composto após a tabela (marca-alvo em "maior frequência" **e** "uso atual", mesma marca).
- Em seguida, funil de **versões/variantes** da marca principal (usa → mais usa → usa atualmente → **pantry check**:
  "Você poderia me enviar uma foto da embalagem do produto que está usando? PROGRAMAÇÃO: INSERIR CAMPO PARA FOTO").

## 5. Funil de lojas / serviços (online, Varejo 267.25.006)

Top of mind (OE, 2–30 caracteres) → Conhecimento espontâneo (lista de 20 caixas abertas) → Conhece estimulado
(RM, **Nenhuma → TERMINATE**) → Consideraria comprar (PIPE Q13) → Já comprou alguma vez (PIPE Q13) → Comprou últimos
6 meses (PIPE) → Comprou últimos 3 meses (PIPE) → Compra com maior frequência (SS) → Preferida (SS) → Pretende comprar
no próximo mês (PIPE consideração) → Rejeita (PIPE Q13 **e não** selecionadas em compra/preferência; se todas,
AUTO PUNCH 99 e pular) → Razões da preferência (`[APPLY IF Q18 = 1 TO 22]`, "E por que [PIPE Q18] é a sua loja
preferida…?").

Depois do funil, **aprofundamento de barreiras** por gap de funil, para a marca-cliente:
- Conhece mas não visitou → "Você não visitou lojas físicas da ____ nos últimos 3 meses. Por quê? [MS]" →
  "E qual destes motivos é o principal…? [SS] (PIPE; SE APENAS 1, AUTO PUNCH E PULAR)".
- Visitou mas não comprou → "Você visitou…, mas não comprou. Por que você não comprou? [MS]" → principal [SS].
- Diagnóstico do motivo → "Você mencionou 'baixa qualidade dos produtos' como razão… O que você quis dizer com isso? [MS]".

## 6. Blocos que seguem o funil (tracking)

1. **NPS por marca** — somente marcas conhecidas (P16/P17), máx. N marcas por praça (definir tabela de marcas por
   praça), marcas em rodízio, + follow-ups 0–8 / 9–10 para a marca-cliente.
2. **Imagem de marca** — "Quais destas marcas de ____ você diria que… (APRESENTAR ATRIBUTOS EM RODÍZIO)
   PROGRAMAÇÃO: MOSTRAR MESMAS MARCAS DA P.NPS E RODIZIAR OS ATRIBUTOS" + colunas Nenhuma / Não sabe (ESPONTÂNEO).
3. **Recall de comunicação** — espontâneo + estimulado em tabela única (Não lembro = 98 na espontânea, Nenhuma = 99 na
   estimulada), seguido de meio ("E onde você viu essa comunicação?") e conteúdo ("Você se lembra sobre o que era…?").
