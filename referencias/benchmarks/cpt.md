# Benchmark — Questionário CPT (Concept & Product Test) Kantar Insights

> Fonte: "Questionário - CPT Kantar Insights.docx" (Drive). Nome do estudo: **"Concept and Meat Test"**. Código de survey B2349008, v1.
> Modo: **CAPI** (entrevista pessoal assistida por tablet, em CLT — central location test, campo terceirizado).
> Duração declarada: **40 minutos** no cabeçalho (abordagem diz "aproximadamente 35 minutos").
> Categoria: **sanduíche de hambúrguer grelhado (fast food)** — conceito de combo "Rebel Whopper" (hambúrguer à base de plantas) a R$26,90.
> Desenho: **Concept stage monádico + Product stage sequencial monádico de 2 produtos** (degustação às cegas de 2 hambúrgueres, pareados em 12 painéis de rodízio com 4 códigos de cor), revelação "à base de plantas" ao final, e preferência pareada.

---

## 1. Sequência de blocos / seções

| # | Bloco | Perguntas |
|---|-------|-----------|
| 1 | **BBC: Filtro** (begin block) | ABORDCAPI, F1 (ramo de atividade), F2 (gênero), F3 (idade), F4 (faixa), F5–F5F (Critério Brasil 2015), F6 (restrições de saúde), F13_Copy_1 (últimos 30 min), F7 (frequência fast food), F8 (redes visitadas), F9 (rejeição de rede), F10 (produtos consumidos), F11 (rejeição de sabores), F12 (rejeição de ingredientes) |
| 2 | Controle de cotas e rodízio | F13 (resumo de cotas), PNL (painel/ordem de produtos) |
| 3 | **BBB: Concept Stage** | CONCEPT_INTRO_MN, PRPURINT, UNIQNESS, PRVALMNY, LIKBILTY, EXCITMNT |
| 4 | **BBD: Product Stage** (repetido para produto 1 e 2) | Q002 (procedimento de degustação), Q068_Copy_1 (buscar código na cozinha), Q1 (opinião geral), Q2 (intenção de compra com preço), Q4 (gostou – aberta), Q5 (não gostou – aberta), Q6 (grid de atributos 7 pts), Exemplo (treino JAR), JCN, VBF, VBC, TKN, Q7b, Q7c, VBG, VBD (JAR), Q065 (transição), Q9 (expectativa), VBH, VBJ (revelação "plant-based") |
| 5 | Comparativo (após os 2 produtos) | Q066 (instrução), P1 (preferência), P2 (por quê), P3 (preferência por atributo) |
| 6 | Hábitos (fim) | QUS1 (visitas 30 dias), Q070, QUS2 (rede mais frequente), QUS3 (rede preferida), Q047 (agradecimento) |
| 7 | Encerramento | FIM01 (autorização de envio da gravação) |

---

## 2. Detalhamento por bloco

### 2.1 Filtro (BBC)
- **ABORDCAPI** — RU. Texto literal: "Bom dia/boa tarde, meu nome é (ENTREVISTADOR(A) DIGA O SEU NOME). Eu faço parte da equipe de pesquisadores da [empresa de campo], que presta serviços para a Kantar. Estamos realizando uma pesquisa sobre SANDUÍCHE DE HAMBÚRGUER GRELHADO que durará aproximadamente 35 minutos e gostaríamos de contar com sua colaboração. Para melhorar nosso controle interno e garantir a veracidade das respostas, esta entrevista poderá ser gravada. Suas respostas farão parte de um estudo confidencial e a sua identidade será preservada. Você aceita participar?" 1 Sim; 2 Não. Instrução: "ENTREVISTADOR: LER SE 'NÃO' AGRADEÇA E ENCERRE".
- **F1: RAMO DE ATIVIDADE** — RM "(ESPONTÂNEA) (RM)". "F1. O(a) sr.(a) ou alguém de sua casa trabalha em alguma dessas áreas?" 1 Agência de propaganda ou publicidade; 2 Jornal\Revista\TV\Rádio; 3 Instituto de pesquisa de mercado; 4 Marketing; 5 Supermercados\Hipermercados; 8 Indústria e distribuição de alimentos; 6 Restaurantes\ Fast Food; 7 Desenvolvimento de novos produtos alimentícios; 96 Nenhuma. Scripter: "SE A RESPOSTA FOR DIFERENTE DE 'NENHUM', ENCERRE".
- **F2: Gênero** — "F2. Qual o seu sexo? (ANOTE SEM PERGUNTAR) (RU)" 1 Masculino; 2 Feminino.
- **F3: Idade** — numérica `Min = 18 | Max = 45`. "F3. Quantos anos você tem?" "Digitar idade".
- **F4: Idade Faixas** — dummy. 1 Menos de 18 → SCREEN OUT; 2 De 18 a 25 anos; 3 De 26 a 35 anos; 5 36-45 anos; 4 46 anos ou mais → SCREEN OUT. "Anotar faixa de acordo com a resposta dada em F3. Se código 1 ou 4 ENCERRAR."
- **F5: Critério Brasil 2015 – ITENS DE CONFORTO** — Grid 14 × 5 (NÃO TEM / 1 / 2 / 3 / 4 ou +). Texto: "F5. Agora vou fazer algumas perguntas sobre itens do domicilio para efeito de classificação econômica. Todos os itens de eletroeletrônicos que vou citar devem estar funcionando, incluindo os que estão guardados. Caso não estejam funcionando, considere apenas se tiver intenção de consertar ou repor nos próximos seis meses. No domicílio tem ______". Itens: automóveis de passeio; empregados mensalistas (≥5 dias/semana); máquinas de lavar roupa (excluindo tanquinho); banheiros; DVD; geladeiras; freezers; microcomputadores; lavadora de louças; micro-ondas; motocicletas; secadoras; televisor em cores; rádio. Instrução: "Entrevistador: É importante que o entrevistado fale em voz alta cada resposta para cada item." Scripter: "Please, fix the quantity title when respondents roll down the screen".
- **F5A** — "A água utilizada neste domicílio é proveniente de?" 1 Rede geral de distribuição; 2 Poço ou nascente; 3 Outro meio.
- **F5B** — "Considerando o trecho da rua do seu domicílio, você diria que a rua é:" 1 Asfaltada/Pavimentada; 2 Terra/Cascalho.
- **F5C** — "Você é o chefe da família? Considere como chefe da família a pessoa que contribui com a maior parte da renda do domicílio." Scripter: "IF CODE 1 'SIM', PLEASE MARK IN F15F SAME ANSWER FROM F15D AND SKIP TO F15H." (pula instrução do chefe).
- **F5D** — grau de instrução do chefe: 1 Analfabeto; 2 Fundamental I incompleto (OU Primário Incompleto); 3 Fundamental I completo / Fundamental II incompleto; 4 Fundamental completo/Médio incompleto; 5 Médio completo/Superior incompleto; 6 Superior completo.
- **F5E** — grau de instrução do respondente (mesma lista). "IF CODE 1 (ANALFABETO), TERMINATE."
- **F5F** — dummy CLASSE: A (45-100); B1 (38-44); B2 (29-37); C1 (23-28); C2 (17-22); D/E (0-16). "TERMINAR SE CÓDIGO 6 (D/E)".
- **F6: RESTRIÇÕES** — RM, "Entrevistador: LER". "F6. Vou ler algumas condições físicas e também produtos/ substâncias e gostaria de saber se você é alérgico/a ou apresenta as seguintes condições: (RM)" 1 Está grávida ou amamentando (NÃO LER- APLICAR APENAS PARA MULHERES); 2 Fazendo dieta/ regime com prescrição médica; 3 É diabético (a) ou tem restrição de açúcar ou glicose; 4 Está gripado ou com dificuldade de sentir cheiro; 5 É alérgico (a) a leite ou seus derivados, incluindo lactose, caseinato, caseína, lactoalbumina e sólidos do leite ou glúten; 6 Hipertensão (pressão alta); 7 Problemas com níveis de colesterol (restrições a frituras) — todos → SCREEN OUT; 96 Nenhuma. "SE SIM PARA QUALQUER ALTERNATIVA DE 1 A 7, ENCERRE".
- **F13_Copy_1 (paladar limpo)** — RM "(LER)". "F13. Você fez alguma das seguintes atividades nos últimos 30 minutos?" 1 Mascou chiclete (goma de mascar); 2 Comeu alguma coisa; 3 Fumou cigarro; 4 Escovou os dentes; 5 Nenhuma das anteriores (NÃO LER) *Exclusive. "SÓ CONTINUAR COM QUEM RESPONDEU 'NENHUMA DAS ANTERIORES'" / "If answer is different than code 5, terminate."
- **F7: FREQUÊNCIA DA CATEGORIA** — RU "(MOSTRAR TABLET) (RU)". "F7. Em média, com que frequência você visita lanchonetes do tipo fast food?" 1 Uma vez por semana ou mais vezes por semana; 2 Uma vez a cada 2 ou 3 semanas; 3 Uma vez por mês; 4 Uma vez a cada 2 ou 3 meses; 5 Uma vez a cada 4 ou 6 meses; 6 Uma vez por ano; 7 Com menos frequência; 8 Nunca. "Se códigos 4,5,6,7 ou 8: encerrar".
- **F8: Brand Buyers / Users** — RM "(MOSTRAR TABLET)". "F8. Qual (is) lanchonetes do tipo fast food você visitou no último mês?" Bob's; Burger King; Habib's; KFC; Mc Donald's; Subway; Giraffas; Outros (Especifique) ×2; 96 Nenhuma. "Se 'Nenhuma das opções acima', encerrar".
- **F9: Rejeição QSR** — RM. "F9. E qual (is) lanchonetes do tipo fast food você rejeita?" "If code 2 is selected, TERMINATE." (rejeita a rede do cliente).
- **F10: Consumo produtos** — RM "(MOSTRAR TELA)". "F10. Quais destes produtos você costuma consumir quando visita uma lanchonete do tipo fast food? Mais algum?" 1 Hamburguer de carne; 2 Hamburguer de frango ou peixe; 3 Batata frita; 4 Onion Rings; 5 Chicken Nuggets; 6 Salada; 7 Sobremesa; 8 Bebidas; 998 Nenhuma → encerra.
- **F11: Rejeição produtos** — RM. "F11. Pensando em produtos que podem ser consumidos em uma lanchonete do tipo fast food, você rejeita algum dos sabores abaixo?" Scripter: "Hide options selected in F10. If code 3 and/or code 4 is selected, TERMINATE." (rejeição de carne/vegetais).
- **F12: REJEIÇÃO INGREDIENTES** — RM. "F12. Agora, pensando em um sanduíche de fast food, quais desses ingredientes você rejeita, ou seja, não come de jeito nenhum?" Pão com gergelim; Queijo; Picles; Ketchup; Alface; Tomate; Cebola; Maionese; 998 Nenhuma. "Se citar um dos códigos, ENCERRE".

### 2.2 Cotas e rodízio
- **F13: RESUMO DE COTAS** — tela "Incluir resumo de: Sexo (F2), Idade (F4), Classe social (F5F)".
- **PNL: PAINEL** — RU. "ENTREVISTADOR: SELECIONE O PAINEL QUE O ENTREVISTADO AVALIARÁ" "(RU)(ATENÇÃO PARA AS COTAS)". 12 painéis = todas as combinações ordenadas de 2 entre 4 produtos codificados por cor:
  - 1 Azul x Amarelo; 2 Amarelo x Azul; 3 Azul x Laranja; 4 Laranja x Azul; 5 Azul x Verde; 6 Verde x Azul; 7 Amarelo x Laranja; 8 Laranja x Amarelo; 9 Amarelo x Verde; 10 Verde x Amarelo; 11 Laranja x Verde; 12 Verde x Laranja.
  - Padrão: **balanceamento de ordem (cada par em ambas as ordens)** — controle de efeito de posição.

### 2.3 Concept Stage (BBB) — monádico, antes da prova
- **CONCEPT_INTRO_MN** — "Show the Concept image." "Agora mostraremos para você algumas informações sobre a ideia de um novo produto. Por favor, olhe e responda as perguntas a seguir."
- Todas com instrução "MOSTRAR TABLET E PEDIR PARA ENTREVISTADO LER A RESPOSTA".
- **PRPURINT** — "Qual dessas frases descreve melhor a probabilidade de você comprar esse combo de Rebel Whopper se ele estivesse disponível?" 1 Definitivamente não compraria; 2 Provavelmente não compraria; 3 Não sei se compraria ou não; 4 Provavelmente compraria; 5 Definitivamente compraria.
- **UNIQNESS** — "Qual dessas frases descreve melhor o quanto você acha que esta ideia de produto é nova e diferente dos outros produtos disponíveis?" Extremamente novo e diferente / Muito novo e diferente / Mais ou menos novo e diferente / Um pouco novo e diferente / Nada novo e diferente.
- **PRVALMNY** — "Considerando o preço do combo Rebel Whopper de R$26,90, qual dessas frases melhor descreve o que você acha dele?" 1 Vale um pouco mais; 2 Vale o que custa; 3 Vale um pouco menos; 4 Vale muito menos; 5 Vale muitíssimo menos.
- **LIKBILTY** — "Qual dessas frases melhor descreve o quanto você acha que gostaria ou não gostaria deste produto?" Gostaria muitíssimo / Gostaria muito / Gostaria / Gostaria um pouco / Não gostaria / Não gostaria nada.
- **EXCITMNT** — "O quanto esta ideia de produto é empolgante\atraente?" Muito empolgante\atraente / Empolgante\atraente / Não muito empolgante\atraente / Nada empolgante\atraente.

### 2.4 Product Stage (BBD) — repetido por produto
- **Q002: Experimentação do produto** — RU. Instrução literal: "ENTREVISTADOR: Explique ao entrevistado o procedimento antes da experimentação do produto. ENTREVISTADOR LER: Você receberá um sanduíche na primeira etapa e outro sanduíche na segunda etapa. Em cada etapa pedimos que você dê 3 mordidas no lanche. Procedimento: Peça para que o entrevistado beba ½ copo de água, coma ½ biscoito de água e beba mais um pouco de água antes de experimentar o produto, explique que a água e o biscoito servem para neutralizar o paladar. ENTREVISTADOR LEIA: Ao receber o produto, por favor, observe todos os aspectos do sanduíche como cor, sabor, aparência, etc." 1 Seguir; 2 Recusa.
  - Scripter: "If code 2 'Recusa' is selected, TERMINATE. Delete the following text for the second product: [...] Include the following text for the second product: ENTREVISTADOR LER: Por favor, experimente esse outro sanduíche. Pedimos que você dê 3 mordidas no lanche."
- **Q068_Copy_1** — "ENTREVISTADOR: BUSCAR O PRODUTO DE CÓDIGO _______ NA COZINHA." Scripter: "Show code according to Q027 question. Put code in red." (código cego do produto conforme painel).
- **Q1** — RU "MOSTRAR TELA". "Q1. Qual é a sua opinião geral sobre este sanduíche? (RU)" 7 Excelente; 6 Muito bom; 5 Bom; 4 Nem ruim, nem bom; 3 Ruim; 2 Muito Ruim; 1 Péssimo. (7 pontos, codificação 7=positivo)
- **Q2** — "Q2. Se este sanduíche estivesse a venda por R$26,90 o combo, qual a probabilidade de você comprá-lo em uma próxima visita em um restaurante Fast-food? (RU)" 5 Definitivamente compraria; 4 Provavelmente compraria; 3 Poderia comprar ou não; 2 Provavelmente não compraria; 1 Definitivamente não compraria.
- **Q4** — Aberta "EXPLORAR". "Q4. Tem algo que você particularmente gosta neste sanduíche? Mais alguma coisa? Por favor: Responda com o máximo de detalhes possível."
- **Q5** — Aberta "EXPLORAR". "Q5. E tem alguma coisa que você particularmente não gosta neste sanduíche? Mais alguma coisa? Por favor: Responda com o máximo de detalhes possível."
- **Q6** — Grid 7 × 7, linhas Random. "Q6. Agora eu gostaria que você avaliasse alguns aspectos específicos neste produto. Como você classifica este sanduíche com relação a:" Escala Péssimo / Muito Ruim / Ruim / Nem ruim, nem bom / Bom / Muito bom / Excelente. Itens: Sabor em geral; Combinação dos ingredientes; Sabor do hambúrguer; Qualidade do hambúrguer; Sabor do hambúrguer que ficou na boca; Textura do hambúrguer; Aparência do hambúrguer.

#### Escala JAR (Just About Right) — treinamento + 8 atributos
- **Exemplo (treino)** — texto literal: "ENTREVISTADOR LEIA: Por favor, antes de fazermos essa parte eu gostaria de lhe mostrar como funciona o registro da sua resposta, por favor, olhe a escala abaixo. Um lado da escala diz 'Muito mais do que eu gosto' enquanto o outro lado diz 'Muito menos do que eu gosto' e há 5 caixas, sendo que a caixa do meio de número 3 indica que está 'na medida certa' ou 'do jeito que você gosta'. Então, se você achar que o produto tem uma dada característica que em sua opinião está mais forte, mais intensa ou maior do que você gosta, você deve indicar os pontos 4 ou 5. Se você achar que essa característica do produto está mais fraca, menor, etc. do que você gosta, você deve indicar os pontos 1 ou 2. Mas se você acha que a característica avaliada está na medida certa ou do jeito que você gosta então você deve indicar o ponto 3." + "Entrevistador: garanta que o respondente compreendeu a escala no exemplo antes de prosseguir".
  - Escala-modelo: Muito mais do que eu gosto / Mais do que eu gosto / Do jeito que eu gosto / Menos do que eu gosto / Muito menos do que eu gosto.
- Atributos JAR (cada um 1 linha × 5 colunas, "MOSTRAR TELA"):
  | ID | Pergunta literal | Rótulos |
  |---|---|---|
  | JCN | "Como você avalia a suculência do hambúrguer deste sanduíche? (RU)" | Muito mais suculento do que eu gosto / Mais suculento... / Do jeito que eu gosto / Menos suculento... / Muito menos suculento do que eu gosto |
  | VBF | "Como você avalia o ponto de preparo do hambúrguer deste sanduíche? (RU)" | Muito mais passado... / Mais passado... / Do jeito que eu gosto / Menos passado... / Muito menos passado do que eu gosto |
  | VBC | "Como você avalia a intensidade de sal deste sanduíche? (RU)" | Muito mais salgado... / Mais salgado... / Do jeito que eu gosto / Menos salgado... / Muito menos salgado... |
  | TKN | "Como você avalia a espessura do hambúrguer deste sanduíche? (RU)" | Muito mais grosso... / Mais grosso... / Do jeito que eu gosto / Mais fino... / Muito mais fino do que eu gosto |
  | Q7b | "Como você avalia a cor do hambúrguer deste sanduíche? (RU)" | Muito mais escuro... / Mais escuro... / Do jeito que eu gosto / Mais claro... / Muito mais claro... |
  | Q7c | "Como você avalia a intensidade do sabor de churrasco do hambúrguer deste sanduíche? (RU)" | Muito mais forte... / Mais forte... / Do jeito que eu gosto / Mais fraco... / Muito mais fraco... |
  | VBG | "Como você avalia a intensidade do sabor do hambúrguer deste sanduíche? (RU)" | idem forte/fraco |
  | VBD | "Como você avalia a maciez do hambúrguer deste sanduíche? (RU)" | Muito mais macio... / Mais macio... / Do jeito que eu gosto / Menos macio... / Muito menos macio... |

- **Q065 (transição)**: "Você continuará avaliando o produto, mas agora as questões terão escalas diferentes." (LER)
- **Q9: Expectativa** — "Q9. Como você avalia a sua experiência com este sanduíche comparada à sua expectativa antes de provar?" 5 Muito melhor do que eu esperava; 4 Um pouco melhor do que eu esperava; 3 É o que eu esperava; 2 Um pouco pior do que eu esperava; 1 Muito pior do que eu esperava.
- **VBH (revelação – intenção)** — "Q12. Sabendo que esse hambúrguer é hambúrguer à base de plantas, isso muda a sua avaliação?" 5 Eu definitivamente compraria ele depois de saber disso; 4 Eu provavelmente compraria...; 3 Isso não mudaria minha opinião; 2 Eu provavelmente não compraria...; 1 Eu definitivamente não compraria ele depois de saber disso.
- **VBJ (revelação – avaliação)** — "Sabendo que esse hambúrguer é um hambúrguer à base de plantas, isso muda a sua avaliação?" 5 Eu avaliei muito melhor; 4 Eu avaliei melhor; 3 Não teve nenhuma influência; 2 Eu avaliei pior; 1 Eu avaliei muito pior.

### 2.5 Comparativo (após os 2 produtos)
- **Q066**: "ENTREVISTADOR: Para as seguintes perguntas não mostrar tela. Ler todas as questões a seguir."
- **P1** — RU "LER". "P1. Levando tudo em consideração, agora que você já provou ambos os produtos, qual deles você estaria mais propenso a comprar?" 1 O primeiro produto que você experimentou - PRODUTO 1; 2 O segundo produto... - PRODUTO 2; 3 Sem preferência- Ambos (ESPONTÂNEO); 4 Sem preferência- Nenhum dos dois (ESPONTÂNEO).
- **P2** — Aberta "LER (EXPLORAR)". "P2. Por que você disse que estaria mais propenso a comprar (insert text)? Mais alguma coisa?" Scripter: "If code 1 in P1 show text: o primeiro produto / If code 2 ...: o segundo produto / If code 3 ...: ambos os produtos / If code 4 ...: nenhum dos dois produtos".
- **P3** — Grid 7 × 4. "P3. Qual produto você prefere, o primeiro ou o segundo produto com relação a:" "LER APENAS ATRIBUTOS NÃO LER AS ESCALAS!" Colunas: PRODUTO 1 / PRODUTO 2 / Sem preferência- Ambos (ESPONTÂNEO) / Sem preferência- Nenhum dos dois (ESPONTÂNEO). Linhas = os 7 atributos de Q6.

### 2.6 Hábitos e encerramento
- **QUS1** — "QUS1. Quantas vezes você foi em qualquer restaurante de fast-food nos últimos 30 dias? (RU)" 1 1 - 3 Vezes; 2 4 - 8 Vezes; 3 9 ou mais vezes.
- **QUS2** — "Qual restaurante de fast-food você visita com mais frequência?" (MOSTRAR TELA) Burger King, Mc Donald's, Bob's, Habib's, KFC, Subway, Giraffas, 996 Outros.
- **QUS3** — "Qual restaurante de fast-food você prefere?" (mesma lista).
- **Q047** — "Muito obrigado por sua participação! Tenha certeza que a sua opinião é muito importante para o desenvolvimento de novos e melhores produtos."
- **FIM01** — "O(a) senhor(a) autoriza o envio da gravação da sua entrevista para a empresa contratante dessa pesquisa?" 1 Sim; 2 Não.

---

## 3. Padrões reutilizáveis
1. **CPT = conceito primeiro, produto depois**: KPIs de conceito (PI, unicidade, value, gostaria, empolgação) medidos ANTES da prova; na prova, repete-se PI com preço para medir o gap conceito × produto; Q9 mede **confirmação de expectativa**.
2. **Rodízio por painéis de cor**: todas as permutações ordenadas de pares (n produtos → n×(n−1) painéis), selecionadas pelo entrevistador com atenção às cotas; produto buscado na cozinha pelo **código cego**.
3. **Protocolo sensorial explícito**: limpeza de paladar (½ copo de água + ½ biscoito de água + água), nº de mordidas (3), observar cor/sabor/aparência; filtro "últimos 30 minutos" (chiclete, comida, cigarro, escovar dentes) e restrições de saúde/alergias como screen out.
4. **Ordem de avaliação do produto**: opinião geral (7 pts) → PI com preço (5 pts) → gostou/não gostou (abertas, "Mais alguma coisa?") → grid de atributos hedônicos (7 pts) → **treino da escala JAR** → atributos JAR (5 pts, ponto 3 = "Do jeito que eu gosto") → expectativa → revelação de informação (plant-based) → após 2 produtos: preferência global, por quê, preferência por atributo.
5. **JAR com rótulos específicos por atributo** (mais suculento/mais salgado/mais grosso/mais escuro etc.), nunca genéricos; entrevistador garante compreensão antes.
6. **Revelação tardia de informação sensível** (ex.: "à base de plantas") só depois das avaliações cegas, medindo impacto em intenção e em avaliação separadamente.
7. **Preferência pareada** com códigos espontâneos "Ambos" e "Nenhum dos dois" (não lidos) e P3 "LER APENAS ATRIBUTOS NÃO LER AS ESCALAS!".
8. **Texto do 2º produto adaptado** via scripter note (remove explicação da 1ª etapa, insere "Por favor, experimente esse outro sanduíche").
9. **CAPI**: marcações de apoio ao entrevistador — (RU)/(RM), (ESPONTÂNEA), (LER)/(NÃO LER), (MOSTRAR TABLET)/(MOSTRAR TELA), "EXPLORAR", "ANOTE SEM PERGUNTAR", "É importante que o entrevistado fale em voz alta".
10. **Critério Brasil 2015 completo** (itens de conforto + água + rua + chefe + instrução) com dummy de classe e screen out D/E; tela de **resumo de cotas** para o entrevistador.
11. Rejeição da marca/rede do cliente e rejeição de ingredientes do produto teste → screen out.
12. Abordagem com consentimento de gravação + pergunta final autorizando envio da gravação ao cliente.
13. Hábitos detalhados (visitas, rede mais frequente, preferida) colocados no FIM para não enviesar a avaliação.
14. Codificação crescente positiva no produto (7=Excelente, 5=Definitivamente compraria) listada de cima para baixo do positivo ao negativo.
