# Benchmark — Questionário Conjoint (Kantar Insights)

> Fonte: "Questionário - Conjoint Kantar Insights.docx" (Drive). Modo: **CAWI** (painel online, parceria Kantar + LightSpeed).
> Categoria: **Gonadotrofinas** (medicamentos de reprodução assistida), público B2B: clínicas (proprietário / gerente de compras / prescritor).
> Duração declarada: **20 minutos**. Formato do documento: template Kantar "Questionnaire" com tabelas por pergunta (ID + rótulo em inglês, tipo, propriedades como `Not back`, `Dummy`, `Min/Max`, `Random`, códigos, e `Scripter notes`).
> Estrutura de exercício: **DCM / CBC (Discrete Choice Model)** dentro do módulo **Value Manager (VM)** da Kantar — avalia equity + preço e depois roda 2 exercícios de escolha (protocolo FSH puro e protocolo combo).

---

## 1. Sequência de blocos / seções

| # | Bloco | Perguntas (IDs na ordem) |
|---|-------|--------------------------|
| 1 | Abordagem | ABORD |
| 2 | Perfil / dados de painel (dummies) | GENDER (F1), AGE (F2), AGE_RNG (F3), UF, CITY, RGN |
| 3 | Qualificação B2B (filtros) | SC6 (Category Buyer), CLIENT1 (papel na compra) |
| 4 | **B006: Value Manager Template** (begin block) | VM_Intro1, VM1 (frequência), VM2 (conhecimento de marca), VM3 (marcas já compradas), VM3 (marcas rejeitadas), VM4 (últimas 5 compras), VM5 (marca mais comprada, desempate), Q079 (dummy marca principal), VM6 (performance), VM7 (preferência), VM8 (percepção de preço), VM9 (percepção de valor), VM10 (estimativa de preço pago), VM_Intro2, VM11 (preço vs. 2ª opção), VM12 (preço vs. preço usual), VM13_Copy_1 (hábitos/atitudes de compra – pares bipolares) |
| 5 | Volume / prescrição (calibração de volume) | VOLUME_1_FSH, VOLUME_2_Protocolo_Combo |
| 6 | **Exercícios de escolha (DCM)** | VM14_CPP – Protocolo FSH puro; VM14_CPP – Protocolo Combo |
| 7 | Diagnóstico pós-conjoint (abertas) | CL1_MAIS FREQUENTE, CL2_MENOS FREQUENTE, CL3_MAISFREQUENTE_COMBO, CL2_MENOS FREQUENTE (combo) |

Observação: a numeração é por ID de variável (não P1, P2…). Todas as perguntas principais são `Not back` (sem voltar).

---

## 2. Detalhamento por bloco

### 2.1 Abordagem (ABORD — Text)
- Objetivo: convite, garantia de confidencialidade/LGPD, duração, pedir resposta de uma vez.
- Texto literal (trecho): "Olá, a Kantar em parceria com a LightSpeed que é uma consultoria independente de pesquisa de mercado está realizando uma pesquisa. A Kantar garante a preservação de identidade, dados de navegação e privacidade dos respondentes durante a pesquisa. Todos os dados coletados pela Kantar são confidenciais, sendo utilizados apenas para fins de pesquisa. Naturalmente, as respostas são anônimas e o sigilo individual está totalmente garantido. Nenhuma informação será divulgada individualizada. A sua opinião é muito importante e para isso pedimos que você clique na seta >> abaixo e responda a um questionário com duração prevista de 20 minutos. Se possível, por favor, responda a pesquisa de uma só vez, pois você não poderá acessar depois. A Kantar agradece desde já a sua colaboração."

### 2.2 Perfil (dados do painel)
- **GENDER: F1. Gênero** — RU. `Not back | Dummy - Não teremos controle de cota para esta pergunta.` "Anotar sexo do entrevistado:" 1 Masculino / 2 Feminino. Scripter: "Information captured by the panel (URL)."
- **AGE: F2** — Numérica. `Min = 18 | Max = 90 | Dummy`. "Qual a sua idade?" Scripter: "If lower than 18 or higher than 90 - TERMINATE the interview and show the termination text: 'Muito obrigado por sua participação, mas estamos procurando pessoas com um perfil diferente do seu'".
- **AGE_RNG: F3. AGE RANGE** — RU dummy ("SCRIPT ONLY. DO NOT SHOW"). 1 Menos de 18 anos → GO TO SCREEN OUT; 2 18-34; 3 35-54; 4 55-74; 5 75-90; 6 Mais de 90 anos → GO TO SCREEN OUT. Scripter: "RECORD THE AGE IN THE CORRECT RANGE PLEASE, CREATE QUOTA WITH THIS QUESTION".
- **UF** — RU "Qual estado você mora?"; **CITY** — "Qual é a sua cidade" (lista MDD; "PLEASE USE MDD TEMPLATE, apply only if UF --> 1"); **RGN** — RU dummy, sem cota: Região Sudeste / Nordeste / Sul / Centro Oeste / Norte.

### 2.3 Qualificação B2B
- **SC6: Category Buyer** — RM, `Min = 1 | Max = 7`. "Qual(is) dos produtos abaixo você comprou nos últimos 3 meses para a sua clínica?" Códigos: 1 Serm; 2 FSH Urinário ou Recombinante; 3 Análogos do GNRH (Agonista / Antagonista); 4 Gonadotrofinas; 5 Inibidores da aromatase; 6 Sensibilizador de insulina; 998 Nenhuma das opções acima *Fixed *Exclusive → GO TO SCREEN OUT.
  - Filtro literal: "If answer code 4 is not chosen --> Screen Out".
- **CLIENT1** — RM. "Qual é a sua atuação na clínica em relação à compra das gonadotrofinas?" 1 Proprietário; 2 Gerente / Supervisor de compras; 3 Prescritor; 998 Nenhuma das opções acima → SCREEN OUT.
  - Scripter literal: "If answer code 998 is not chosen --> Screen Out" (erro de redação no original — a lógica pretendida é encerrar SE 998).

### 2.4 Bloco B006 — Value Manager Template (equity + preço)
Objetivo: medir funil de marca (conhecimento → compra → rejeição), share das últimas compras, índice TRIM (performance + preferência), percepção de preço e valor, conhecimento de preço e atitudes de compra — insumos para calibrar o modelo de escolha.

- **VM_Intro1 (Text)**: "A próxima pergunta é sobre Gonadotrofinas. Por favor, pense somente nesta categoria de produto."
- **VM1: CATEGORY PURCHASE FREQUENCY** — RU. "Em média, com que frequência você costuma comprar esta categoria?" Escala: 1 Todo dia; 2 Duas vezes na semana; 3 Uma vez por semana; 4 Uma vez a cada duas semanas; 5 Uma vez por mês; 6 Uma vez a cada 2 meses; 7 Com menor frequência.
- **VM2: BRAND AWARENESS** — RM, `Min = 1`, Random. "Qual (is) destas marcas você conhece pelo menos de nome?" Marcas: 1 Gonal; 2 Pergoveris; 3 Elonva; 4 Puregon; 5 Merional; 6 Menopur; 7 Rekovelle; 998 Nenhuma (Fixed/Exclusive) → SCREEN OUT.
- **VM3: BRANDS EVER BOUGHT** — RM, Random. `Min = 1 - SHOW ALL KNOWN BRANDS (ACC. TO VM2)`. "Qual(is) destas marcas você já comprou?" 998 Nenhuma → SCREEN OUT.
- **VM3: REJECT BRANDS** — RM, Random. "Qual(is) destas marcas você rejeita?" Códigos 1 Gonal e 2 Pergoveris → GO TO SCREEN OUT (rejeitadores das marcas do cliente são excluídos); 998 Nenhuma.
- **VM4: LAST FIVE PURCHASES** — Soma constante (`Sum`, `Max sum = 5 - Use mentioned answers from VM3`). Texto literal: "Pensando nas últimas 5 compras desta categoria de produto, quantas vezes você comprou cada uma dessas marcas? Por favor, lembre-se que o total das marcas compradas deve ser igual a 5 e se você não tiver comprado alguma dessas marcas nas suas últimas 5 compras, por favor preencha com campo desta marca com 0 (zero)." Scripter: "This question is heavily edited. Please do not change unless you really Need to."
- **VM5: MAINLY BOUGHT BRAND** — RU. "E qual destas marcas você compra mais frequentemente?" (lista + 996 Outros (especifique)). Filtro literal: "ONLY ASKED IF 2 OR MORE BRANDS RECEIVED THE SAME HIGHEST SCORE IN VM4 (LAST 5 PURCHASES)" — pergunta de desempate.
- **Q079: DUMMY CONTROL FOR MOST FREQUENT Brand** — RU dummy. Scripter: "(Brands control) hardcode answer from VM5 or highest scored brand from VM4 - DUMMY. We must have this question as a control, so we will need to see it in quotas".
- **VM6: TRIM INDEX QUESTION 1: PERFORMANCE** — Grid (7 linhas × 5 colunas), linhas Random. "Considerando todos os aspectos, como você avalia o desempenho dessa marca?" Escala: **Ruim / Regular / Bom / Muito bom / Excelente**. "Rendered as Dynamic Grid - SHOW MAINLY BOUGHT BRAND ACCORDING TO VM4/VM5. SHOW PICTURE".
- **VM7: TRIM INDEX QUESTION 2: PREFERENCE** — Grid 7×5, Random. "O quanto você prefere esta marca em comparação com as outras que existem atualmente?" Escala: **Sem preferência / Um pouco / Fortemente / Muito fortemente / Extremamente forte**. "SINGLE CODE PER BRAND".
- **VM8: BRAND PRICE PERCEPTION** — Grid, Random. "Como você avalia o preço desta marca em comparação com as outras que existem atualmente? Comparado com outras marcas o preço desta marca é…" Escala: **Muito mais baixo / Mais baixo / Mais alto / Muito mais alto** (4 pontos, sem ponto médio). Scripter: "ASK FOR ALL KNOWN BRANDS (ACC. TO VM2). SHOW BRANDS IN RANDOMISED ORDER IN A GRID OR ON SEPARATE SCREENS. SINGLE CODE PER BRAND."
- **VM9: BRAND VALUE PERCEPTION** — Grid, Random. "E como você se sente em relação ao valor desta marca (não ao preço) em comparação com as demais marcas disponíveis atualmente? Comparada com as demais marcas disponíveis, a marca é..." Escala: **Vale muito menos / Vale menos / Vale mais / Vale muito mais**.
- **VM10: PRODUCT PRICE ESTIMATION** — Alfa/numérica. "Quanto você pagou pelo produto considerando um ciclo de tratamento de 10/12 dias, entre 2000 e 2700 unidades que comprou na última vez direto do distribuidor? Se não se lembrar, dê uma estimativa." Scripter: "SHOW TWO BOXES LIKE THIS: __ , __ REAIS ... First box should start the range from 1."
- **VM_Intro2 (Text)**: "A próxima pergunta ainda é sobre Gonadotrofinas. Por favor, pense no produto que você comprou na última vez"
- **VM11: RELATIVE PRICE KNOWLEDGE 1 (COMPETITOR PRICES)** — RU. "Comparado com a segunda escolha que você consideraria comprar, o preço que pagou na última compra era maior ou menor?" 1 Não sei dizer; 2 O preço era menor; 3 O preço era maior; 4 O preço era igual.
- **VM12: RELATIVE PRICE KNOWLEDGE 2 (PRICES OVER TIME)** — RU. "Ainda pensando no produto que você comprou da última vez, comparado ao preço que este produto normalmente custa, na última compra você pagou mais ou menos?" (mesmos códigos de VM11).
- **VM13_Copy_1: BUYING HABITS AND ATTITUDES** — Left-right matrix, 9 pares, escala de 2 pontos (1 | 2), RU por par. Pares literais:
  1. "Acho que as marcas diferem muito" × "Acho que todas as marcas são mais ou menos o mesmo"
  2. "Eu sempre sei exatamente a marca que vou comprar" × "Eu nunca sei exatamente a marca que vou comprar"
  3. "Eu sempre compro a marca que comprei na última vez" × "Sempre compro uma marca diferente"
  4. "Sempre comparo os preços com cuidado" × "Geralmente não comparo preços"
  5. "Eu procuro especificamente ofertas especiais" × "Eu nunca procuro ofertas especiais"
  6. "Eu sempre sei o preço dos produtos que compro" × "Realmente nunca sei o custo dos produtos"
  7. "Estou sempre interessado em produtos novos" × "Prefiro ficar com o que eu conheço"
  8. "Nenhum dos produtos disponíveis atualmente realmente atende às minhas necessidades" × "Estou completamente satisfeito (a) com a gama de produtos que estão disponíveis atualmente"
  9. "Eu acho fácil fazer a escolha certa para minha clínica" × "Eu acho muito difícil fazer a escolha certa minha clínica"
  - Scripter literal: "Do not allow for 'don't know' answers! Do not show a rating scale! Statement pairs shall be shown in the order as displayed here (with no rotation). This will make it easier for respondents to understand subtle differences between statements. // SCRIPTING: SHOW PAIRS OF STATEMENTS IN UNROTATED ORDER. SINGLE CODE PER STATEMENT PAIR".

### 2.5 Volume de prescrição (calibração)
- **VOLUME_1_FSH** — grade numérica. "Considerando um protocolo FSH puro, qual desses medicamentos você indica para sua paciente em um tratamento usual de 10/12 dias entre 2000 e 2250 UI?" Colunas: Protocolo FSH PURO | Dose Diária | Total de doses no Ciclo. Linhas: Gonal, Puregon, Elonva, Rekovelle. Scripter: "(Soma de todas as doses será o que o médico irá prescrever para a paciente aplicar ao total do tratamento.)"
- **VOLUME_2_Protocolo_Combo** — "Considerando um protocolo combo (FSH+LH/HMG), quais desses medicamentos você indica para sua paciente em um tratamento usual de 10/12 dias entre 2000 e 2700 UI?" Colunas: Protocolo Combo | Dose Diária | Total de doses no Ciclo. Linhas: Gonal, Puregon, Elonva, Rekovelle, Menopur, Merional, Pergoveris.
- Objetivo: traduzir escolha em unidades/doses (volume) para simulação de share em volume.

---

## 3. Exercícios de escolha (DCM / Conjoint)

### 3.1 Estrutura
- **Dois exercícios independentes**, cada um com seu próprio set de marcas (atributo "marca") e preços:
  - **Exercício 1 – Protocolo FSH puro**: marcas Gonal, Puregon, Elonva, Rekovelle.
  - **Exercício 2 – Protocolo Combo (FSH+LH/HMG)**: Gonal, Puregon, Elonva, Rekovelle, Pergoveris, Menopur e Merional.
- **Atributos**: marca/produto × **preço** (conjoint de marca-preço / "Brand-Price Trade-Off" em formato DCM). A unidade de compra é fixada no texto ("ciclo completo… 10/12 dias entre 2000 e 2250 UI" / "2000 e 2700 UI").
- **Opção "nenhum"**: sim — "Você poderá escolher entre uma das opções que aparecerem ou nenhuma delas."
- **Nº de tarefas, nº de conceitos por tela, níveis de preço**: NÃO estão no questionário — Scripter literal: **"DCM LEVEL PLAN IS PROVIDED SEPARATELY IN EXCEL SPREADSHEET"**. (Ou seja, o desenho experimental — matriz de níveis, versões, tarefas — é documento à parte.)
- Contexto de compra: canal = distribuidor; ancoragem na última compra real.

### 3.2 Texto de introdução — Protocolo FSH puro (VM14_CPP, literal)
"Agora, gostaríamos que você imaginasse que vai comprar Gonadotrofinas diretamente de um distribuidor para realizar um protocolo FSH puro. Você verá uma série de situações de compras desse produto, marcas e preços diferentes e gostaria que você escolhesse qual produto você compraria. Imagine que a cada situação você terá diferentes opções para sua escolha. Você poderá escolher entre uma das opções que aparecerem ou nenhuma delas. O importante é que você imagine que está fazendo uma compra real, como se estivesse realmente desembolsando este valor na compra de Gonadotrofinas FSH, sem nenhuma outra droga combinatória ou substituta. Leve em consideração que a compra que você irá realizar será para um ciclo completo, ou seja, para o tratamento de uma pessoa com duração aproximada de 10/12 dias entre 2000 e 2250 UI. Por favor, pense na sua última compra. Se estas fossem todas as opções disponíveis naquela ocasião, qual produto você teria comprado?"

### 3.3 Texto de introdução — Protocolo Combo (literal)
"Agora, gostaríamos que você imaginasse que vai comprar Gonadotrofinas diretamente de um distribuidor para realizar um protocolo combo.(FSH+LH/HMG). Você verá uma série de situações de compras desse produto, marcas e preços diferentes e gostaria que você escolhesse qual produto você compraria em cada uma das situações. Imagine que a cada situação você terá diferentes opções para sua escolha. Você poderá escolher entre uma das opções que aparecerem ou nenhuma delas. O importante é que você imagine que está fazendo uma compra real, como se estivesse realmente desembolsando este valor na compra de Gonadotrofinas Leve em consideração que a compra que você irá realizar será para um ciclo completo, ou seja, para o tratamento de uma pessoa com duração aproximada de 10/12 dias entre 2000 e 2700 UI. Por favor, pense na sua última compra. Se estas fossem todas as opções disponíveis naquela ocasião, qual produto você teria comprado?"

### 3.4 Elementos-chave do texto de instrução do conjoint (checklist)
1. Situação imaginada concreta (quem compra, onde, para quê).
2. "Você verá uma série de situações" (múltiplas tarefas).
3. Marcas e preços variam entre telas.
4. Permissão explícita de "nenhuma delas".
5. Realismo econômico: "como se estivesse realmente desembolsando este valor".
6. Delimitação da unidade de compra (ciclo completo, UI).
7. Ancoragem na última compra: "Se estas fossem todas as opções disponíveis naquela ocasião, qual produto você teria comprado?"

---

## 4. Diagnóstico pós-exercício (abertas)
- **CL1_MAIS FREQUENTE** — Aberta. "Agora, pensando na marca mais frequente que você selecionou que comprou no exercício de FSH Puro, qual o motivo de prescrever com maior frequência o medicamento _____ ." Scripter: "PUXAR A RESPOSTA MAIS FREQUENTE DO EXERCÍCIO PROTOCOLO 1".
- **CL2_MENOS FREQUENTE** — Aberta. "E, qual o motivo de prescrever com menos frequência o medicamento ______________ ?" Scripter: "PUXAR A RESPOSTA MENOS FREQUENTE DO EXERCÍCIO PROTOCOLO 1".
- **CL3_MAISFREQUENTE_COMBO** — Aberta. "Agora, pensando na marca mais frequente que você selecionou que comprou no exercício de combo de FSH+LH/HMG, qual o motivo de prescrever com maior frequência os medicamentos _____ e _____." Scripter: "PUXAR A RESPOSTA MAIS FREQUENTE DO EXERCÍCIO PROTOCOLO COMBO".
- **CL2_MENOS FREQUENTE (combo)** — idem, "PUXAR A RESPOSTA MENOS FREQUENTE DO EXERCÍCIO PROTOCOLO COMBO".
- Objetivo: explicar as escolhas do modelo com verbatims (piping da marca mais/menos escolhida nas tarefas).

---

## 5. Bases e filtros (resumo)
| Pergunta | Base |
|---|---|
| SC6, CLIENT1 | Total entrevistados |
| VM1–VM2 | Qualificados (compram gonadotrofinas e têm papel na compra) |
| VM3 (comprou) | Marcas conhecidas em VM2 |
| VM3 (rejeita) | Total qualificado; rejeita Gonal/Pergoveris → encerra |
| VM4 | Marcas já compradas (VM3) — soma = 5 |
| VM5 | Só se empate na maior pontuação de VM4 |
| VM6/VM7 | Marca principal (VM4/VM5), com imagem |
| VM8/VM9 | Todas as marcas conhecidas (VM2) |
| VM14 (2 exercícios) | Total qualificado |
| CL1–CL4 | Total; piping da marca mais/menos escolhida em cada exercício |

---

## 6. Padrões reutilizáveis
1. **Conjoint precedido de módulo de equity/preço** (Value Manager): funil de marca → share últimas N compras → marca principal → performance + preferência (TRIM) → percepção de preço e de valor → conhecimento de preço → atitudes de compra. Só então o exercício de escolha.
2. **Share of last N purchases** como soma constante (N=5 em B2B; conceito usa 10) com instrução literal de "preencha com 0 (zero)" para marcas não compradas; pergunta de **desempate** só quando há empate no máximo.
3. **Dummy de marca principal** (hardcode de VM5 ou maior score de VM4) usada como **cota/controle**.
4. **Rejeitadores da marca do cliente → screen out** antes do exercício.
5. **Preço vs. valor separados**: perguntar percepção de preço (4 pontos, sem meio) e, à parte, valor "(não ao preço)" (4 pontos).
6. **Conhecimento de preço** em duas perguntas: vs. 2ª opção considerada e vs. preço usual do mesmo produto, sempre com "Não sei dizer" como código 1.
7. **Pares bipolares sem rotação e sem "não sei"** para atitudes de compra (propensão a troca, sensibilidade a preço, abertura a novidade, satisfação com a oferta) — insumo de "inércia/propensão a trocar".
8. **Unidade de compra explícita** no texto do conjoint (ciclo, UI, peso) para evitar ambiguidade de preço.
9. **Texto padrão do conjoint** com: série de situações, opção "nenhuma", compra real com dinheiro próprio, ancoragem na última compra.
10. **Desenho experimental fora do questionário**: o questionário referencia "DCM LEVEL PLAN IS PROVIDED SEPARATELY IN EXCEL SPREADSHEET" (tarefas, conceitos/tela, níveis, versões).
11. **Vários exercícios por sub-mercado** (ex.: protocolo puro vs. combo) com set de marcas próprio e texto de introdução adaptado.
12. **Calibração de volume** (doses/unidades por marca) antes ou junto do exercício, para converter preferência em volume.
13. **Abertas pós-exercício com piping** da alternativa mais e menos escolhida ("PUXAR A RESPOSTA MAIS FREQUENTE DO EXERCÍCIO...").
14. **Termo de encerramento padrão**: "Muito obrigado por sua participação, mas estamos procurando pessoas com um perfil diferente do seu".
15. Faixa etária como dummy "SCRIPT ONLY. DO NOT SHOW" derivada da idade numérica, com os extremos em SCREEN OUT e instrução "CREATE QUOTA WITH THIS QUESTION".
16. Convenções de códigos: 996 = Outros (especifique), 998 = Nenhuma das opções acima (*Fixed *Exclusive), marcas em ordem Random.
