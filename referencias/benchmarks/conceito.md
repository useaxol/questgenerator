# Benchmark — Questionário Teste de Conceito (Kantar Insights / eValBuilder)

> Fonte: "Questionário - Conceito Kantar Insights.docx" (Drive). Título interno: "Cow Tradicional e Chocolate SP – eValBuilder" — cliente de biscoitos (marca Toddy).
> Modo: **CAWI**. Plataforma/metodologia: **eValBuilder** (Kantar, módulos padronizados "Growth Tool Module").
> Categoria: **biscoitos secos doces / rosquinhas**. Praça: **São Paulo** (Sudeste/SP apenas).
> Desenho: **sequencial monádico de 2 conceitos** (Conceito 1 – Rosquinhas sabor Toddy; Conceito 2 – Rosquinhas Toddy com gotinhas de sabor de chocolate). A mesma bateria de avaliação é repetida para cada conceito.

---

## 1. Sequência de blocos / seções

| # | Bloco | Perguntas |
|---|-------|-----------|
| 1 | **M002: Demographic Screener** (Growth Tool Module) | SEG, SEG_Agrupado, GENDER, AGE, AGE BANDS, REGION, UF |
| 2 | Segurança | SECTOR_INDUS_SCREENING |
| 3 | Categoria | CATBUYER, CATFRQ, VBG (quem compra) |
| 4 | Marca | BRDBUY, DUMMY_TODDY, PST10PUR_TEXT (últimas 10 compras) |
| 5 | Introdução de conceito | CONCEPT_INTRO_MN (Conceito 1), CONCEPT_INTRO_SQ2 (Conceito 2) |
| 6 | KPIs centrais | PRPURINT (intenção de compra com preço), UNIQNESS |
| 7 | **B003: Price perception** | PRVALMNY |
| 8 | Aceitação / frequência | LIKBILTY, PURCHFRQ |
| 9 | **B004: Incrementality** | INCREMNT, PRTINCR_RESP |
| 10 | Diagnósticos | RELVANCE, EXCITMENT, UNDERSTG, BELVBLTY |
| 11 | Volume | PURVOL, UNTVAR_TEXT |
| 12 | Diagnóstico qualitativo | LIKES, DISLIKES, HIGHLIGHTER_DRIVERS_TEXT, HIGHLIGHTER_BARRIERS_TEXT |
| 13 | Imagem de marca | CONC_IMG_1 |
| 14 | **Inércia de categoria** | INERTIA_INTRO, INERTIA_1, INERTIA_2, INERTIA_3 |

Blocos 6–13 repetem-se para cada conceito (sequencial). Inércia é perguntada uma vez (nível categoria).

---

## 2. Detalhamento por bloco

### 2.1 Screener demográfico (M002)
- **SEG** — RU dummy do painel ("SEG CLASSIFICATION FROM PAINEL"): 1 A; 2 B1; 3 B2; 4 C1; 5 C2; 6 D/E → GO TO SCREEN OUT. Scripter: "PLEASE CONSIDER THAT THE PANEL WILL PASS THE 'SEC' VALUES FROM 1 TO 6 AND WE NEED TO RECODE CODES 1-3 TO 'AB' (code 1 at this question) AND CODES 4-5 TO 'C' (code 2 at this question). PLEASE SCREEN OUT IF CODE 6."
- **SEG_Agrupado** — dummy: 1 AB; 2 C ("If code 1, 2 or 3 in SEG: Allocate the respondent to code 1 in SEG_Agrupado / If code 4 or 5 in SEG: Allocate ... code 2").
- **GENDER** — "Você é...?" 1 Homem; 2 Mulher.
- **AGE** — numérica `Min = 18 | Max = 65`. "Qual é a sua idade?"
- **AGE BANDS** — 1 17 anos ou menos → Screen out; 2 18-29 anos; 3 30-49 anos; 4 50-65 anos; 6 66 anos ou mais → Screen out. "If code 1 or code 6, please screen out."
- **REGION** — "Onde você mora?" 1 Norte; 2 Nordeste; 3 Centro Oeste; 4 Sul (todos → GO TO SCREEN OUT); 5 Sudeste.
- **UF** — "Qual estado você mora?" 1 São Paulo; 2 Rio de Janeiro; 3 Espírito Santo; 4 Minas Gerais (2–4 → SCREEN OUT).

### 2.2 Segurança
- **SECTOR_INDUS_SCREENING** — RM. "Você ou alguém na sua casa trabalha em alguma dessas áreas?" 1 Marketing, design ou pesquisa de mercado; 2 Relações públicas; 4 Propaganda / Publicidade; 5 Jornalismo ou mídia; 6 Fabricação ou distribuição de comida; 7 Venda no varejo ou atacado de comida; 8 Desenvolvimento de novos produtos; 997 Nenhuma destas *Fixed *Exclusive. Client note: "only 'None of the above' response is eligible".

### 2.3 Categoria
- **CATBUYER: Category Buyers / Users** — RM, Random. "Quais desses produtos você comprou nos últimos 3 meses para você?" 1 Biscoitos recheados doces; 2 Biscoitos salgados; 3 Biscoitos secos doces (sem recheio); 4 Biscoitos rosquinhas; 5 Biscoitos tipo maisena; 997 Nenhuma destas.
- **CATFRQ** — RU. "Com que frequência você compra biscoitos secos doces para você?" 1 Uma vez por semana ou mais; 2 Uma vez a cada 2-3 semanas; 3 Uma vez por mês; 4 Uma vez a cada 2-3 meses → SCREEN OUT; 5 Uma vez a cada 4-6 meses → SO; 6 Uma vez por ano → SO; 7 Com menos frequência → SO; 8 Nunca → SO. (Qualifica: compra ao menos mensal.)
- **VBG: Compra** — "Quem costuma comprar os biscoitos secos doces na sua casa?" 1 Somente eu; 2 Eu e outra(s) pessoa(s); 3 Somente outra(s) pessoa(s) → SCREEN OUT.

### 2.4 Marca
- **BRDBUY** — RM, Rotated. "Quais marcas de biscoitos secos doces você comprou nos últimos 3 meses para você?" 1 Bauducco Cereale; 2 Marilan; 3 Piraquê; 4 Mãe Terra; 5 Triunfo; 6 Toddy; 7 Visconti; 8 Belvita; 996 Outras *Fixed.
- **DUMMY_TODDY** — dummy "code 6 – Toddy at question BRDBUY" (usuário da marca do cliente, para leitura/cota).
- **PST10PUR_TEXT: Past 10 Purchases** — Soma constante `Min sum = 10 | Max sum = 10`, Rotated. "Pensando nas suas últimas 10 compras de biscoitos secos doces. Quantas foram de cada marca abaixo?"

### 2.5 Introdução do conceito (sequencial)
- **CONCEPT_INTRO_MN** — CONCEITO 1 – ROSQUINHAS SABOR TODDY: "Agora você vai ver algumas informações sobre uma ideia de um novo produto. Por favor, veja as informações e responda as perguntas seguintes."
- **CONCEPT_INTRO_SQ2** — CONCEITO 2 – ROSQUINHAS TODDY COM GOTINHAS DE SABOR DE CHOCOLATE: "Agora você vai ver algumas informações sobre uma outra ideia de um novo produto. Por favor, veja as informações e responda as perguntas seguintes."
- Várias perguntas trazem `{thumbnail}` — miniatura do conceito na tela da pergunta.

### 2.6 KPIs centrais
- **PRPURINT: Priced Purchase Intention** — RU. "Qual a probabilidade de você comprar este produto para você se ele estiver disponível no local que você faz suas compras?" Escala: 1 Definitivamente não compraria; 2 Provavelmente não compraria; 3 Não sei se compraria ou não; 4 Provavelmente compraria; 5 Definitivamente compraria.
  - Client note literal: "Order of response scale shown to respondents is different to above. 'Definitely would buy' is shown in first position; 'Definitely would not buy' is shown in last position." (codificação ≠ ordem de exibição).
- **UNIQNESS** — RU. "Quão novo e diferente você acha que este produto é de outros(as) biscoitos secos doces disponíveis?" 1 Extremamente novo e diferente; 2 Muito novo e diferente; 3 Mais ou menos novo e diferente; 4 Pouco novo e diferente; 5 Nada novo e diferente.

### 2.7 B003: Price perception
- **PRVALMNY: Priced Value For Money** — RU. "O que você acha sobre o preço desse produto?" 1 Vale um pouco mais; 2 O preço está correto; 3 Vale um pouco menos; 4 Vale menos; 5 Vale muito menos. (Escala assimétrica, pesada para o lado negativo.)

### 2.8 Aceitação e frequência
- **LIKBILTY: Likability** — "Qual dessas frases melhor descreve o quanto você gostou ou não deste produto?{thumbnail}" 1 Gostei muitíssimo; 2 Gostei muito; 3 Gostei; 4 Gostei mais ou menos; 5 Gostei pouco; 6 Não gostei nada. (6 pontos)
- **PURCHFRQ** — "Com que frequência você compraria este produto se estivesse disponível?{thumbnail}" 1 Uma vez por semana ou mais; 2 Uma vez a cada 2-3 semanas; 3 Uma vez por mês; 4 Uma vez a cada 2-3 meses; 5 Uma vez a cada 4-6 meses; 6 Uma vez por ano; 7 Com menos frequência; 8 Nunca.

### 2.9 B004: Incrementality (canibalização)
- **INCREMNT** — RU. "Se você fosse a uma loja hoje para comprar este produto e não o encontrasse, o que você compraria no lugar dele?" 1 Compraria outro(a) biscoitos secos doces da marca Toddy; 2 Compraria uma marca diferente de biscoitos secos doces; 3 Não compraria um biscoito secos doces se este produto não estivesse disponível.
- **PRTINCR_RESP: Portfolio Incrementality - Sequential only** — RU, Rotated. "E de qual marca seria?" (lista de marcas de BRDBUY). Client note: "Filtered on INCREMNT: Code 2".

### 2.10 Diagnósticos
- **RELVANCE** — "Quão relevante é este produto?" 1 Nada relevante; 2 Pouco relevante; 3 Mais ou menos relevante; 4 Muito relevante; 5 Extremamente relevante.
- **EXCITMENT** — "Quanto você acha que esse produto é empolgante?" 1 Muito empolgante; 2 Empolgante; 3 Não muito empolgante; 4 Nada empolgante.
- **UNDERSTG: Understanding / Clarity** — Left-right slider 9 pontos. "Com base no que você leu sobre esse produto, deslize para o ponto nessa escala que reflete como você se sente:" Polo esquerdo "Eu não sei o que esperar desse produto" ↔ direito "Eu sei exatamente o que esperar desse produto".
- **BELVBLTY: Believability / Credibility** — "Até que ponto você acredita no que foi mostrado sobre esse produto?" 1 Acredito muito; 2 Acredito um pouco; 3 Não acredito muito; 4 Não acredito nada.

### 2.11 Volume
- **PURVOL: Purchase Volume** — numérica `Min = 0 | Max = 100`. "No total, quantas unidades você compraria desse produto por vez?" Client note: "A maximum of SIX varieties per concept can be managed by this module. If a concept has more than 6 varieties, custom scripting is required."
- **UNTVAR_TEXT: Units by Variety** — Soma (`Max sum = 100`). "Você mencionou que compraria {incluir resposta questão PURVOL} por vez que fosse comprar este produto. Quantos(as) desses(as) seriam de cada variedade listada abaixo?" 980 Total; 1 Toddy 30 gr; 2 Toddy 40 gr; 3 Toddy 200 gr; 4 Toddy 400 gr.

### 2.12 Diagnóstico qualitativo
- **LIKES** — Aberta: "O que você GOSTOU nesta ideia?"
- **DISLIKES** — Aberta: "O que você NÃO GOSTOU nesta ideia?"
- **HIGHLIGHTER_DRIVERS_TEXT** — "Abaixo está a imagem do novo produto novamente. Por favor, clique nas áreas da tela que você GOSTOU."
- **HIGHLIGHTER_BARRIERS_TEXT** — "Abaixo está a imagem do novo produto novamente. Por favor, clique nas áreas da tela que você NÃO GOSTOU."

### 2.13 CONC_IMG_1: Concept Imagery (marca)
- Grid, linhas Random. "Aqui estão algumas declarações que foram usadas para descrever esta ideia. O quanto você concorda ou discorda de cada uma delas?"
- Escala: **Concordo totalmente / Concordo em parte / Nem concordo nem discordo / Discordo em parte / Discordo totalmente**.
- Itens: Combina com a marca Toddy; Combina com a imagem que tenho dos produtos de Toddy; Deixa a impressão de que a marca Toddy busca entender seus consumidores; Deixa a impressão de que a marca Toddy é inovadora; Toddy me surpreende positivamente; Toddy tem produtos únicos e diferenciados; Toddy tem variedade de produtos.
- Nota: "Info on deliverables: (a) A maximum of 8 statements".

### 2.14 Inércia da categoria (propensão a experimentar)
- **INERTIA_INTRO**: "Gostaríamos de fazer algumas perguntas sobre {biscoitos} em geral"
- **INERTIA_1** — left-right 7 pontos. "Qual dessas frases melhor descreve como você se sente ao escolher um (a) novo (a) {INERTIACATEGORY} pela primeira vez?"
  - "É muito barato para eu me preocupar com isso" ↔ "É muito caro, já que posso não gostar depois de ter comprado"
  - "Eu não me preocupo com o que outras pessoas pensam sobre produtos novos antes de comprá-los" ↔ "Eu não compraria um produto novo até que outras pessoas me dissessem que o produto é bom"
- **INERTIA_2** — "Como você se sente ao escolher um(a) {biscoito} geralmente?"
  - "Sei exatamente qual marca vou escolher" ↔ "Eu não escolho a marca que vou comprar até que eu veja todas as opções"
  - "Eu sempre escolho a mesma marca" ↔ "Eu sempre escolho uma marca diferente"
- **INERTIA_3** — "Como você se sente sobre as opções de {biscoitos} disponíveis atualmente?"
  - "Estou totalmente satisfeito(a) com os produtos disponíveis atualmente" ↔ "Atualmente não existe nenhum produto que atenda as minhas necessidades"

---

## 3. Bases e filtros (resumo)
| Pergunta | Base |
|---|---|
| Screener | Total; 18–65, AB/C, SP, sem conflito de setor, compra biscoito seco doce ≥ mensal, é comprador |
| PST10PUR | Qualificados (marcas de BRDBUY) |
| KPIs, diagnósticos, volume | Total por conceito (sequencial: todos avaliam C1 e C2) |
| PRTINCR_RESP | INCREMNT = cód. 2 |
| UNTVAR | Total, soma = resposta de PURVOL |
| Inércia | Total, uma vez |

---

## 4. Padrões reutilizáveis
1. **Ordem canônica de avaliação de conceito (Kantar)**: intro → **Intenção de compra (com preço) → Unicidade → Value for money → Gostar → Frequência → Incrementalidade → Relevância → Empolgação → Clareza → Credibilidade → Volume (unidades/variedade) → Likes/Dislikes abertas → Highlighter (clique) → Imagem de marca → Inércia**.
2. **KPI de compra sempre primeiro** após a exposição (evita contaminação por diagnósticos).
3. **Codificação ≠ ordem de exibição**: codificar 1=negativo…5=positivo mas exibir "Definitivamente compraria" primeiro (nota explícita ao programador).
4. **Value for money com escala assimétrica** (1 ponto positivo, "O preço está correto", 3 negativos) — padrão eValBuilder para conceito com preço.
5. **Incrementalidade em 2 passos**: o que compraria no lugar (mesma marca / outra marca / não compraria) → se outra marca, qual.
6. **Clareza em slider bipolar 9 pontos** e **credibilidade 4 pontos** sem neutro.
7. **Volume em 2 passos**: unidades por ocasião (0–100) → distribuição por variedade/tamanho (soma = total), máx. 6 variedades por módulo.
8. **Highlighter (clique em áreas) de drivers e barreiras** depois das abertas de gostou/não gostou.
9. **Imagem de marca pós-conceito** (concordância 5 pontos, até 8 frases, ordem aleatória) — mede halo do conceito sobre a marca.
10. **Inércia de categoria** em pares bipolares 7 pontos: risco percebido, influência social, lealdade/decisão, satisfação com a oferta — usada para ajustar previsões.
11. **Last 10 purchases** (soma constante = 10) para share de marca e dummy de usuário da marca do cliente.
12. **Recodificação de classe social** vinda do painel (1–3 → AB, 4–5 → C, 6 → screen out) como dummy de cota.
13. **Sequencial monádico**: textos de introdução diferentes para 1º ("uma ideia de um novo produto") e 2º conceito ("uma outra ideia").
14. `{thumbnail}` do conceito repetido nas perguntas de avaliação para manter o estímulo presente.
15. Screener de setor com "você ou alguém na sua casa" e só "Nenhuma destas" elegível.
