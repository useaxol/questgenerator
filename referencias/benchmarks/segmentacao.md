# Benchmark — Questionário de Segmentação (Kantar "Matrix" – Need States por ocasião)

> Fonte: "Questionário - Segmentação Matrix - Kantar Insights.docx" (Drive). Título interno: "25b Matrix survey example 2017 Edition — Matrix Survey Shell — Beverages example".
> Natureza: **shell/modelo** (em inglês) de questionário de **segmentação de necessidades por ocasião (demand spaces / need states)** — categoria exemplo: bebidas. Cada seção traz Objetivo ("Purpose") e Considerações ("Considerations"); o texto abaixo traduz/resume e cita verbatim as perguntas.
> Observação do documento: "Please note that category specific shells for many categories are also available through your Matrix expert."

---

## 1. Sequência de seções

| Seção | Nome | Perguntas | Usada no modelo? |
|---|---|---|---|
| 1 | Screener | (flexível) | Não |
| 2 | Usage scan | Q201, Q202, Q203, Q204, Q205 | Só para dimensionamento (sizing) |
| 3 | Occasion selection & focus | Q301, Q302, Q303, Q304, Q305 | Não (contexto) |
| 4 | **Need** (ideal) | Q401, Q402 | **Sim — base da segmentação** |
| 5 | **Image** (entrega dos produtos) | Q501 | **Sim — mapeia produtos aos segmentos** |
| 6 | Lifestyle & beliefs (opcional) | Q601 | Opcional (perfil / segmentação de consumidor) |
| 7 | Other category understanding / U&A (opcional) | livre | Não (sem suporte do time Matrix) |

---

## 2. Detalhamento por seção

### Seção 1 — Screener
- "This section is flexible and may be adapted to the unique requirements of your study." (Livre; segue padrões do estudo.)

### Seção 2 — Usage scan
- **Objetivo** (trad.): levantar o uso dos produtos no escopo para **selecionar uma ocasião recente** na qual o respondente vai focar ao responder as necessidades ideais; quando o cliente quer segmentos dimensionados em volume/valor, esses dados suportam o sizing.
- **Considerações**: NÃO usada na modelagem (exceto sizing); perguntas podem ser adaptadas desde que meçam frequência e identifiquem uma ocasião recente qualificada; "In high frequency categories a 'recent' occasion is typically one that has taken place in the past 24/48 hours (but this can be flexible)".
- **Q201: Ever consumed** — RM. "Which of the following have you ever consumed? (Select all that apply)" Lista de produtos + "None of the above [Terminate]" (99).
- **Q202: Consumed past month** — RM. "Which of the following have you consumed in the past month? (Select all that apply)" — "[Ask only of products ever consumed]". 99 None → Terminate.
- **Q203: Consumption frequency** — grid RU por produto. "For those you have consumed in the past month, how frequently do you typically consume them? (Select one response for each)" — "[Ask only of products consumed in past month]". Escala (7 pts): Once a day or more often / 4-6 times a week / 2-3 times a week / Once a week / Once every 2-3 weeks / Once a month / Less often than once a month.
- **Q204: Consumption momentum** — grid RU. "Compared to a year ago, how often do you currently consume each of the following? (Select one response for each)" — "[Ask only of products consumed in past month]". Escala: More often / About the same / Less often.
- **Q205: Consumed recently** — RM. "Which of the following have you consumed in the past 24 hours? (Select all that apply)" — "[Ask only of products consumed in past month]". "None of the above [Terminate]".

### Seção 3 — Occasion selection & focus
- **Objetivo**: garantir que a mente do respondente esteja focada em **uma única ocasião específica e recente**, usada como contexto para as necessidades ideais → necessidades mais granulares, não genéricas.
- **Considerações (literal/trad.)**:
  - Informação NÃO usada na modelagem.
  - Perguntas estilo **5W** ("where were you, what were you doing, who was with you, what else did you consume, etc."); "Only ~3-4 questions need to be asked to ensure proper focus".
  - "Each respondent should only be asked to focus on ONE occasion. Data quality diminishes if respondents are asked about multiple occasions."
  - **Métodos de seleção da ocasião foco**:
    - **LEAST FILLED** — focar na ocasião mais recente do produto com menos entrevistas até o momento (recomendado).
    - **QUOTA** — metas (mínimos/máximos) de ocasiões por produto conforme objetivos (ex.: garantir mínimo de ocasiões com bebida de iogurte).
    - **RANDOM** — sorteio entre produtos recentes; "this approach is not recommended, as there could be bias according to when the interview is completed".
  - Pode-se usar critério secundário (período do dia, dia da semana) para mix representativo.
  - Os segmentos são **reponderados** pela participação real de consumo (ex.: se 5% das ocasiões são de iogurte líquido mas 10% das ocasiões foco, down-weight).
- **Q301: Time of day** — RM. "When exactly was it that you consumed [insert product consumed recently] in the past 24 hours? (Select all that apply)" — "[Ask once for each product consumed in the past 24 hours]". Faixas: 6 AM – 8 AM / 8 AM – 11 AM / 11 AM – 2 PM / 2 PM – 5 PM / 5 PM – 8 PM / 8 PM – 11 PM / 11 PM – 6 AM.
- **Q302: Focus occasion assignment** — lógica: "[Select one focus occasion per respondent according to criteria outlined for this study]". Texto exibido: "For the next few questions, please think about the most recent time you consumed [insert focus product] between [insert time of day]."
- **Q303: Day part** — RU. "Which of the following best describes the most recent time you consumed [insert focus product] between [insert time of day]. (Select one response only)" Before breakfast / At breakfast / After breakfast/ as a mid-morning snack / At lunch / After lunch/ as an afternoon snack / At dinner / After dinner/ as an evening snack / Late night/ as a mid-night snack.
- **Q304: Location** — RU. "Where were you the most recent time you consumed [insert focus product] between [insert time of day]. (Select one response only)" At home / At work/ school / At a restaurant/ cafe / At a mall/ out shopping / At the park/ beach / At the gym / In transit / Somewhere else.
- **Q305: With whom** — RM. "Who were you with the most recent time you consumed [insert focus product] between [insert time of day]. (Select all that apply)" Spouse/ partner / Parents / Other adult family member / Children under 18 / Friends/ colleagues / Nobody else – by myself [Exclusive].

### Seção 4 — Need (necessidades IDEAIS) — núcleo da segmentação
- **Objetivo**: respondente descreve a solução **IDEAL** para a ocasião foco avaliando a importância de uma lista abrangente de benefícios → usado no modelo para gerar os **segmentos de necessidade por ocasião**.
- **Considerações**: "The set-up of this question is standard and should NOT be changed unless pre-agreed with Matrix team". Cada respondente vê só um **subconjunto (~40 benefícios)** conforme **versões** definidas após fechar a lista.
- **Texto introdutório (literal)**: "Please continue thinking carefully about the most recent time you consumed [insert focus product] between [insert time of day], which you described when answering the previous questions. We would like to know which characteristics are important to you when choosing your IDEAL product for this type of situation. Please keep in mind that, while it might feel that way sometimes, every characteristic can't be equally important to you in this type of situation, so please try to avoid using the same scale point for all/ most characteristics. Please be sure to consider all answer choices before rating each one."
- **Q401: Need (part one)** — grid RU por benefício. "Thinking about your IDEAL product for this type of situation, how important is each characteristic below? (Select one response for each)"
  - Escala (5 pts): **Extremely Important (5) / Very Important (4) / Fairly important (3) / Somewhat important (2) / Not at all important (1)**.
  - Programação literal: "[Show benefits according to version assigned. Please control for an equal number of exposures of each benefit list version to as representative a mix of respondents as possible. Benefits on the assigned version should be shown one screen at a time, in a random order.]"
- **Q402: Need (part two)** — desempate de "tudo importante".
  - Filtro literal: "[Ask only if (a) more than half the benefits shown in the previous question are rated as 'extremely important', OR (b) no benefits are rated as 'extremely important' but more than 50% of benefits are rated as 'very important'.]"
  - Texto: "You mentioned that many characteristics are extremely important to you in choosing your ideal product for this type of situation. We would now like you to separate them into two groups based upon importance for this type of situation: Absolutely critical and Less critical. This will help us to understand your needs better. (Select one response for each)"
  - Escala: **Absolutely critical (2) / Less critical (1)**.
  - Programação: "[If part two is asked, show only benefits (a) rated as 'extremely important' OR (b) rated as 'very important' if no benefits are rated as 'extremely important'. Benefits should be shown one screen at a time.]"
- Referência: "(2)(8) Matrix Scripting Best Practices guidelines".

### Seção 5 — Image (entrega percebida dos produtos)
- **Objetivo**: indicar quais produtos atuais "definitivamente entregam" cada benefício (mesma lista da Seção 4) → posicionar produtos nos segmentos.
- **Considerações**: setup padrão, não alterar; subconjunto de ~40 benefícios e **~12 produtos** por respondente, por versões.
- **Q501: Image** — grid RM (benefício × produtos). Texto literal: "For the next question, we would like your opinions of various products based on what you know or have heard about them, even if you have never used them yourself. For each characteristic shown, select all products you believe DEFINITELY HAVE this characteristic. You may select as many or as few as apply, or none if you feel no product definitely has the characteristic. (Select all that apply)" Colunas: Product 1…n + "None of these" (99).
  - Programação literal: "[Show benefits according to version assigned – same version shown at Need (part one) above. Benefits on the assigned version should be shown one screen at a time, in the same random order shown at Need (part one) above.]" / "[Show products according to version assigned. Please control so each product list version is shown together with each benefit list version an equal number of time to as representative a mix of respondents as possible. Products on the assigned version should be displayed so they are all visible on the screen without scrolling.]"

### Seção 6 — Lifestyle & beliefs (opcional)
- **Objetivo**: bateria de afirmações de crenças, comportamentos e tensões de estilo de vida (**BBLs**) para perfilar usuários/grupos; em desenhos mais profundos pode gerar **segmentação de consumidor**.
- **Considerações**: todos veem todas as BBLs — ~10-12 (desenho básico) ou ~30 (profundo). Se o cliente tem segmentação existente, pode-se usar **golden questions** para classificar o respondente.
- **Q601** — grid RU. Texto literal: "For the next few questions, we're interested in learning more about you as a person. Please indicate how strongly you agree or disagree with each of the statements below. Please keep in mind that we want to learn about you. You are a very interesting person and we want you to use the statements below to describe what makes you so distinctive, so please avoid using the same scale point for all/ most of your responses. The more statements you rate with the same scale point, the more challenging it is for us to understand you as an individual. (Select one response for each)"
  - Escala: **Strongly agree (5) / Somewhat agree (4) / Neither agree nor disagree (3) / Somewhat disagree (2) / Strongly disagree (1)**.
  - Programação: "[Show all BBL statements to all respondents. Statements should be shown one screen at a time, in a random order.]"

### Seção 7 — U&A adicional (opcional)
- "Where time/ budget allows, additional questions (e.g. usage and attitudes) can added to the end of the survey to address additional project goals. The Matrix team will provide no support on this section."

---

## 3. Bases e filtros (resumo)
| Pergunta | Base |
|---|---|
| Q202 | Produtos já consumidos (Q201) |
| Q203/Q204/Q205 | Produtos consumidos no último mês (Q202) |
| Q301 | Uma vez por produto consumido nas últimas 24h |
| Q303–Q305 | Ocasião foco atribuída (1 por respondente) |
| Q401 | Versão de benefícios atribuída (~40) |
| Q402 | Só se >50% "Extremely important" OU (nenhum extremely e >50% "Very important"); mostra só esses benefícios |
| Q501 | Mesma versão de benefícios de Q401 + versão de produtos (~12) |
| Q601 | Total (todas as BBLs) |

---

## 4. Tradução sugerida (PT-BR) das escalas-chave
- Importância: Extremamente importante / Muito importante / Razoavelmente importante / Um pouco importante / Nada importante.
- Desempate: Absolutamente crítico / Menos crítico.
- Imagem: "selecione todos os produtos que você acredita que DEFINITIVAMENTE TÊM esta característica" + "Nenhum destes".
- Concordância: Concordo totalmente / Concordo em parte / Nem concordo nem discordo / Discordo em parte / Discordo totalmente.

---

## 5. Padrões reutilizáveis
1. **Arquitetura de segmentação por ocasião**: screener → usage scan (sempre / último mês / frequência / momentum / últimas 24h) → seleção de UMA ocasião foco → 3–4 perguntas 5W de imersão → necessidades IDEAIS → imagem de produtos nos mesmos benefícios → (opcional) BBLs → (opcional) U&A.
2. **Uma única ocasião por respondente**, a mais recente, selecionada por **least filled** (preferido) ou quota; evitar random. Reponderar segmentos pela participação real de consumo.
3. **Piping da ocasião** em todas as perguntas ("the most recent time you consumed [product] between [time of day]").
4. **Necessidade ideal ≠ avaliação de marca**: perguntar "IDEAL product for this type of situation", não o produto consumido.
5. **Instrução anti-straightlining** explícita antes das grades de importância e BBLs ("every characteristic can't be equally important… avoid using the same scale point").
6. **Desempate de importância** (Q402) quando >50% no topo — reclassifica em "Absolutamente crítico / Menos crítico".
7. **Versões balanceadas de listas** (~40 benefícios, ~12 produtos) com exposições iguais e cruzamento balanceado benefícios × produtos.
8. **Um item por tela, em ordem aleatória**; a grade de imagem reutiliza a mesma ordem aleatória da grade de necessidade.
9. **Imagem em formato "pick-any"** (associação livre benefício → produtos, com "None of these"), baseada em conhecimento/ouvir falar, mesmo sem uso.
10. Grade de produtos visível **sem scroll**.
11. **Golden questions** para reproduzir segmentação existente do cliente.
12. Seções de modelagem (Need/Image/BBL) são **padrão e não se alteram** sem acordo com o time de modelagem; seções de contexto são flexíveis.
13. Frequência de consumo em 7 pontos (de "1x/dia ou mais" a "menos de 1x/mês") e momentum em 3 pontos (mais/igual/menos que há um ano).
14. "None of the above [Terminate]" nos filtros de consumo (Q201/Q202/Q205).
