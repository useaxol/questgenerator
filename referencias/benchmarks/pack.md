# Benchmark — Questionário Pack Test (Kantar Insights)

> Fonte: "Questionário - Pack Kantar Insights.docx" (Drive). Rodapé: "U0910003- Pack Tester Gaia | version 1 | © Kantar".
> Modo: **CAWI** (Kantar + LightSpeed). Idioma PT-BR. Duração: **20 minutos**. Versão 1.
> Categoria: **sabão em pó para lavar roupa** (marca teste: Omo; variantes Lavagem Perfeita e Puro Cuidado, 800g).
> Desenho: **monádico com 4 células** (gôndola atual × nova, variante Lavagem Perfeita × Puro Cuidado) — cada respondente vê UMA gôndola e UMA embalagem teste.

---

## 1. Sequência de blocos / seções (índice do documento)

| # | Bloco | Perguntas |
|---|-------|-----------|
| 1 | Abordagem + introdução | ABORD, Introd |
| 2 | Filtro de dispositivo | SCA (Devices) |
| 3 | Perfil / cotas | VBB (região), SC4 (classe), Q039 (classe agrupada), SC1 (gênero), SC3 (idade), AGE_RNG |
| 4 | Segurança e responsabilidade | SC2 (ocupação), SC5 (grocery shopping), F5 (responsável pela compra), F5 (responsável pela lavagem), Q041 (máquinas por semana) |
| 5 | Categoria e marca | PCS (compra de produtos), PCS_FRQ, CONHCMTO (conhecimento), BRD (compra), FRQ_BRAND (mais frequente), RJC (rejeição), Q042 (canais) |
| 6 | **B001: Tarefa de Compra** (bloco) | SCTG (célula/gôndola dummy), VR1 (intro shopping), VR2 (exercício de compra na gôndola) |
| 7 | Pós-compra (diagnóstico da escolha) | Q045 (facilidade), Q45A (razões RM), Q45B (razão principal), Q046 (decidido × aberto), Q047 (stand out / lembrança) |
| 8 | **Findability (find time)** | VR3_TEXT, TIMER_START_VR3, VR3, TIMER_END_VR3, Q047A |
| 9 | Exposição rápida (5 s) e elementos lembrados | Q048 (intro), Q048_IMAGE, VR4 (Pack elements – top 3) |
| 10 | Barreiras | VR5 (se não comprou a embalagem teste) |
| 11 | Avaliação da embalagem (monádica, com pack na tela) | VR6 (PI), VR7 (frequência), VR8A (value for money), VR8B (gostar), Q7A/Q067 (heatmap likes + aberta), Q7B/Q068 (heatmap dislikes + aberta), VR8 (eye catching), VR9 (uniqueness), VR9A (interesse), VR10 (brand fit), Q049 (atributos de produto), VR13 (imagem de marca) |
| 12 | Avaliação do claim isolado | Q048A (intro claim), VR8B_claim, VR8_claim, VR13A (imagem de marca pós-claim) |

(Índice também lista VR12 Quality e VBC Preferência, que não aparecem no corpo.)

---

## 2. Detalhamento por bloco

### 2.1 Abordagem e introdução
- **ABORD (Text)** — mesmo padrão Kantar: "Olá, a Kantar em parceria com a LightSpeed é uma consultoria independente de pesquisa de mercado e está realizando uma pesquisa sobre sabão para lavar roupa. [...] responda a um questionário com duração prevista de 20 minutos. Se possível, por favor, responda a pesquisa de uma só vez, pois você não poderá acessá-las depois."
- **Introd (Text)**: "Você será convidado a participar de uma simulação de compra para uma pesquisa e você necessitará utilizar certos aparelhos de comunicação"

### 2.2 SCA: Devices (filtro técnico)
- RU. "Qual desses aparelhos você está usando no momento para acessar a Internet?"
- 1 Computador Tradicional; 2 Laptop/Notebok; 3 Tablet (ex.Apple Ipad, Galaxy Tab, etc); 4 Um e-reader (ex. Kindle) → GO TO SCREEN OUT; 5 Uma TV ou Video Game Console → SCREEN OUT; 6 Smartphone de Tela Grande → SCREEN OUT; 7 Smartphone de Tela Pequena → SCREEN OUT.
- Racional: gôndola virtual exige tela grande — **smartphone é excluído**.

### 2.3 Perfil / cotas
- **VBB** — RU "Onde você mora?" 1 Região Sul; 2 Sudeste; 3 Nordeste; 4 Norte; 5 Centro-Oeste.
- **SC4: Classe** — dummy do painel: 1 A (45-100); 2 B1 (38-44); 3 B2 (29-37); 4 C1 (23-28); 5 C2 (17-22); 6 D/E (0-16) → SCREEN OUT. "This information will come from panel vendor".
- **Q039: Classe Agrupada** — dummy: 1 AB; 2 C. Scripter: "If code 1, 2 or 3 is selected at SC4 = Code 1 / If code 4 or 5 is selected at SC4 = Code 2".
- **SC1: Gênero** — "Você é :" 1 Homem; 2 Mulher. Scripter: "If code 1 screen out" (só mulheres).
- **SC3: AGE** — numérica `Min = 25 | Max = 55`. "Qual a sua idade?"
- **AGE_RNG** — dummy "SCRIPT ONLY. DO NOT SHOW": 1 Menos de 25 → SCREEN OUT; 2 25-35; 3 36-45; 4 46-55; 5 Mais de 55 → SCREEN OUT. "SET AGE_RNG ACCORDING TO AGE".

### 2.4 Segurança, responsabilidade, uso
- **SC2** — RM. "Você trabalha em alguma dessas áreas?" 1 Agência de propaganda ou publicidade; 2 Jornal\Revista\TV\Rádio; 3 Instituto de pesquisa de mercado; 4 Marketing; 5 Indústria ou distribuição de produtos de limpeza; 6 Hipermercado e Supermercado (todos → SCREEN OUT); 998 Nenhuma (*Fixed *Exclusive). "IF SELECT ANY ALTERNATIVE FROM 1 TO 6, SCREEN OUT".
- **SC5: Grocery Shopping** — RU. "Das compras de produtos para o seu domicilio o quanto você costuma fazer?" 1 Todas as compras; 2 Grande parte das compras; 3 Metade das compras; 4 Menos da metade das compras → SCREEN OUT; 5 Nenhuma → SCREEN OUT.
- **F5: RESPONSÁVEL PELA COMPRA** — "Quem é o responsável pela compra de produtos para lavar roupa na sua casa?" 1 Eu mesmo; 2 Eu e outra(s) pessoa(s); 3 Somente outra(s) pessoa(s) → SCREEN OUT.
- **F5: RESPONSÁVEL PELA LAVAGEM** — "Quem é o responsável por lavar as roupas da sua casa?" mesmos códigos; 3 → SCREEN OUT.
- **Q041: Frequency** — "Quantas máquinas de roupa você lava por semana na sua casa?" 1 1 máquina → SCREEN OUT; 2 2 máquinas → SCREEN OUT; 3 3 máquinas; 4 4 máquinas; 5 Mais de 4; 6 Não lavo minhas roupas na máquina → SCREEN OUT.

### 2.5 Categoria e marca
- **PCS: PURCHASE** — RM. "Qual (is) desses produtos você costuma comprar para lavar roupa na sua casa?" 1 Sabão em pó; 2 Sabão líquido; 3 Amaciante; 4 Sabão de coco em barra; 998 Nenhuma. Scripter: "If code 1 is not selected, TERMINATE. If code 1 and 2 are selected, apply next question".
- **PCS_FRQ** — RU. "Você disse que costuma comprar sabão em pó e líquido mas qual deles você costuma comprar com mais frequência para lavar roupa na sua casa?" 1 Sabão em pó; 2 Sabão líquido → SCREEN OUT.
- **CONHCMTO: BRAND AWARENESS** — RM, Random. "Quais marcas de sabão para lavar roupa você conhece pelo menos de nome?" 12 marcas (Omo, Surf, Tixan, Comfort, Ariel, Brilhante, Ala, Assim, Mon Biju, Coquel, Vida Macia, Roma) + 998 Nenhuma → SCREEN OUT.
- **BRD: BRAND BOUGHT** — RM, Random. "Quais destas marcas de sabão para lavar roupa você costuma comprar para sua casa?" "Show only answers selected in CONHCMTO."
- **FRQ_BRAND** — RU. "Qual dessas marcas de sabão para lavar roupa você compra com mais frequência para sua casa?" Scripter: "Show only answers selected in BRD. We will have brand control- make this question as a quota".
- **RJC: BRAND REJECTION** — RM. "E das marcas de sabão para lavar roupa que você conhece, qual(is) você rejeita, ou seja, não compra de jeito nenhum?" "Show answers from CONHCMTO."
- **Q042: Channels Bought** — RM. "Quais os locais onde você costuma comprar sabão para lavar roupa?" 1 Super/ Hipermercado; 2 Mercado de bairro; 3 Mercearias; 4 Atacadão (Exemplo: Sam's Club, Makro); 996 Outros (Especifique) *Open *Fixed.

---

## 3. Exposição à embalagem, prateleira, find time

### 3.1 Alocação de célula — SCTG: Gondola (dummy)
"[SHOW THE SHELF THAT WILL BE APPLIED FOR THE RESPONDENT] Gôndola e embalagem a ser visualizada:"
- 1 Current Shelf Omo + Current Lavagem perfeita – 100
- 2 Current Shelf Omo + Current Puro Cuidado – 100
- 3 New Shelf Omo + New Lavagem perfeita – 100
- 4 New Shelf Omo + New Puro Cuidado – 100
(n = 100 por célula; monádico).

### 3.2 Exercício de compra (B001: Tarefa de Compra)
- **VR1: Shopping Task Intro** (literal): "Imagine que você está indo em um supermercado comprar produtos para você e sua casa, e sabão em pó está na sua lista. Faça o exercício de compra como você normalmente faria. Enquanto você estiver comprando, tenha em mente que: • O produto pode ou não estar disponível, como quando você visita uma loja regular; • Compre como se você estivesse usando o seu próprio dinheiro; • Gaste o tempo necessário, como faria quando faz compra de sabão em pó;"
- **VR2: Purchase Exercise** — [SHOW SHELF]. Scripter literal: "IF SCTG=1 or 2 show image Current Omo Shelf / IF SCTG=3 or 4 show image New Omo Shelf. Need to store order of respondent selection (we need to know the first bought and then the others boughts). There must be a purchase, the respondent cannot proceed without answering/ buying something."
- Tempo de exposição: livre ("Gaste o tempo necessário"). Registro da ordem de compra (1ª compra = produto de referência).

### 3.3 Diagnóstico da compra
- **Q045: Easy to Shop** — RU. "Quão fácil foi encontrar [ANSWER FROM VR2] neste exercício de compra?" 1 Nada fácil; 2 Não muito fácil; 3 Fácil; 4 Muito fácil. "Bring first bought product in VR2".
- **Q45A** — RM, Random. "Quais são todas as razões de você ter escolhido para comprar [ANSWER FROM VR2] ao invés de outros produtos durante a sua compra?" Lista: 1 Porque tem uma embalagem muito diferente do que eu estou acostumado; 2 Porque tem a embalagem mais atrativa; 3 Porque está com embalagem nova; 4 Porque confio na marca; 5 Porque é o produto que estou acostumada a comprar; 6 Porque é o que eu e minha família gostamos; 7 Porque é o mais barato, dentre os que eu gosto; 8 Porque tem um bom custo benefício; 9 Porque me parece sofisticado; 10 Porque tem mais qualidade; 11 Porque parece uma marca que limpa melhor; 998 Nenhuma.
- **Q45B** — RU. "E qual foi o motivo mais importante que fez com que você escolhesse [ANSWER FROM VR2] ao invés de outro?" Scripter: "Bring the drivers chosen in Q45A for first product at VR2. If only one driver is chosen in Q45A, skip Q45B".
- **Q046: Open and Decided** — RU. "Qual afirmação melhor descreve como você tomou a decisão de compra quando estava comprando sabão em pó?" 1 Eu já sabia qual marca comprar antes de começar o exercício, e foi ela que comprei; 2 Eu comecei o exercício querendo comprar uma marca, mas acabei comprando outra; 3 Eu tinha mais de uma marca em mente e tomei a decisão durante o exercício de compra; 4 Eu não tinha nenhuma marca em mente e tomei a decisão durante o exercício de compra.
- **Q047: Stand Out (visibilidade/lembrança)** — RM. "Quais destes produtos você se lembra de ter visto no exercício de compra? Selecione somente aqueles que tem certeza de ter visto." 17 SKUs (Comfort rosa/azul, Omo Puro Cuidado, Omo Lavagem Perfeita, Omo Sanitizante, Omo Sports, Brilhante verde 800g/Cores/Coco/Amaciante, Tixan Ypê Azul/Rosa, Surf Coco/Limão/Lavanda/Rosas, Assim) + 998. "[SHOW BRANDS AS IMAGES]".

### 3.4 Findability (find time)
- **VR3_TEXT** (literal): "Agora gostaríamos que você encontrasse um produto que estava na prateleira onde fez a compra de sabão em pó. Quando você clicar no botão >>> você verá novamente a prateleira e deverá fazer a compra do produto ABAIXO o mais rápido que puder. Por favor, não avance sem ter encontrado o produto abaixo. [SHOW PACK]"
- **TIMER_START_VR3** — "[Start of calculating TIME of question VR3 - Findability]"
- **VR3: Findability** — [SHOW SHELF] (gôndola da célula).
- **TIMER_END_VR3** — "[END of calculating TIME of question VR3 - Findability]"
- **Q047A** — RU. "Quão fácil ou difícil foi encontrar a embalagem?" 1 Muito Fácil; 2 Fácil; 3 Não muito fácil; 4 Nada Fácil.
- Métrica: tempo em segundos entre timers (find time) + facilidade declarada.

### 3.5 Exposição rápida (impacto / elementos lembrados)
- **Q048: Pack Elements Intro** (literal): "A embalagem de um produto muitas vezes pode transmitir certas impressões e criar expectativas específicas para um produto, mesmo se você ainda não teve a chance de experimenta-lo. Quando você pressionar o botão abaixo a embalagem que você acabou de procurar aparecerá por alguns segundos e depois desaparece. Nós, então, queremos saber o que mais chamou a sua atenção nessa embalagem. Pressione o botão abaixo quando estiver pronto."
  - Scripter: "WHEN >> button is pressed, show the Product Omo on the screen for **5 seconds** and then remove it. Go to the next question".
- **VR4: Pack Elements** — Grid ranking (linhas Random × 3 colunas: **Mais lembrado / Segundo mais lembrado / Terceiro mais lembrado**). "Quais partes da embalagem que você acabou de ver foram as mais lembradas? Pense sobre os elementos que ficaram mais em sua mente." Elementos: As cores da embalagem; Ativo concentrado; Rende 10 lavagens; Ciclo de produto mais consciente; Lavagem perfeita; Imbatível na limpeza; Não deixa resíduos; Pó ultrafino; Puro Cuidado; Toque de Aveia; Bebê dormindo; Com impacto positivo no mundo; Hipoalergênico.
  - Filtro por célula (literal): "IF SCTG=1 ... show codes 1, 2, 3, 5 and 7 / IF SCTG=2 ... show codes 1, 2, 3, 9, 10, 11 and 13 / IF SCTG=3 ... show codes 1, 2, 3, 4, 5, 6, 7, 8 and 12 / IF SCTG=4 ... show codes 1, 2, 3, 4, 6, 9, 10, 11, 12 and 13" — lista de elementos só com o que existe em cada embalagem.

### 3.6 Barreiras
- **VR5: Barriers of Purchase** — RU, Random. "Você não escolheu [insert text according to scripter notes] no exercício de compra. Qual destas razões melhor descreve o motivo pelo qual você não o pegou?" 1 Eu não vi; 2 Esta não é a marca que eu geralmente compro; 3 É muito caro; 4 Eu não gostei dessa embalagem; 5 Está diferente do que estou acostumado / Não reconheci; 6 Eu já experimentei e não gostei. Filtro: "IF NOT BOUGHT 'Omo Lavagem perfeita' or 'Omo Puro Cuidado' at VR2 apply this question".

---

## 4. Avaliação monádica da embalagem (pack exibido em todas as telas)
Scripter repetido em todas: "IF SCTG=1 show PACKAGE Current Lavagem perfeita_800g / IF SCTG=2 ... Current Puro Cuidado_800g / IF SCTG=3 ... New Lavagem perfeita_800g / IF SCTG=4 ... New Puro Cuidado_800g".

| ID | Texto literal | Escala (rótulos literais) |
|---|---|---|
| VR6: PI | "Se este produto estiver disponível onde você regularmente compra sabão em pó para você ou para sua casa, qual seria a probabilidade de comprá-lo?" | 1 Definitivamente não compraria / 2 Provavelmente não compraria / 3 Poderia ou não comprar / 4 Provavelmente compraria / 5 Definitivamente compraria |
| VR7: Purchase frequency | "Qual dessas frases melhor descreve quantas vezes compraria esse produto, caso estivesse disponível para venda?" — **Filtro: "Apply this question only if code 4 or 5 at VR6"** | Uma vez por semana ou mais / Uma vez a cada 2 a 3 semanas / Uma vez por mês / Uma vez a cada 2 ou 3 meses / Uma vez a cada 4 ou 6 meses / Menos frequentemente |
| VR8A: Value for money | "Considerando o preço desse produto de R$7,20 com 800 gramas, qual das frases abaixo melhor descreve o que você acha desse produto a esse preço?" | Vale muitíssimo menos / Vale um pouco menos / Vale o que custa / Vale um pouco mais / Vale muitíssimo mais |
| VR8B: Like or Dislike | "Considerando a nota 5 sendo \"gosto muito\" e 1 \"não gosto nada\", qual nota você daria para essa embalagem?" | 1 a 5 |
| Q7A: HeatMap_Likes | "Usando o mouse, por favor, selecione os elementos que você mais gostou ou achou mais atraente na embalagem." — "INSERT TOOL: HEATMAP INCLUDE THE OPTION: \"Gostei de tudo\"" | clique |
| Q067: LIKES (aberta) | "Pensando nos pontos que você selecionou, o que você mais gostou na embalagem? Por quê? Caso tenha selecionado \"Gostei de tudo\" na pergunta anterior, por favor, nos especifique o que você mais gostou na embalagem." | aberta |
| Q7B: HeatMap_Dislike | "Ainda usando o mouse, por favor, selecione os elementos que você menos gostou ou achou menos atraente na embalagem." — opção "Não gostei de nada" | clique |
| Q068: DISLIKES (aberta) | "Ainda pensando nos pontos que você selecionou, o que você menos gostou na embalagem? Por quê? Caso tenha selecionado \"Não gostei de nada\"..." | aberta |
| VR8: Eye Catching | "Pensando especificamente nessa embalagem, de que forma essa embalagem prendeu sua atenção comparado a outras embalagens de sabão em pó?" | Prendeu muito menos a atenção que as outras embalagens / Prendeu um pouco menos... / Prendeu a mesma atenção... / Prendeu um pouco mais... / Prendeu muito mais a atenção que outras embalagens |
| VR9: Uniqueness | "O quanto é diferente e inovadora essa embalagem comparada a outras embalagens de sabão em pó?" | Nada inovadora e diferenciada / Não muito... / Um pouco... / Muito inovadora e diferenciada |
| VR9A: Package | "Quão interessante você achou essa embalagem?" | Nada Interessante / Não muito Interessante / Pouco Interessante / Muito Interessante |
| VR10: Brand Fit | "Para você, até que ponto essa embalagem combina com a marca Omo?" | 1 Não conheço essa marca / 2 Não combina nada / 3 Não combina muito bem / 4 Combina um pouco / 5 Combina bem / 6 Combina completamente |
| Q049: Product Features | "Agora irão aparecer uma série de palavras ou frases que poderão ser utilizadas para descrever esse produto. Qual (is) delas você pensa que melhor se aplica ao produto?" (RM, Random) | É um produto que tem uma embalagem que chama atenção / que vale o quanto custa / com embalagem prática / mais sustentável/ ecológico / de confiança / que me traz sensação de cuidado / 998 Nenhuma |
| VR13: Brand Imagery | "Continue pensando sobre essa embalagem, qual das descrições abaixo você pensa que pode ser usada para descrever a marca Omo?" (RM, Random) | É uma marca que eu confio / sustentável / que vale o quanto custa / fácil de reconhecer na gôndola / de qualidade / que cuida das minhas roupas / diferente das outras / que limpa muito bem / que remove manchas muito bem / 998 Nenhuma |

### 4.1 Avaliação do claim isolado
- **Q048A (Text)**: "Sabemos que uma embalagem é composto por diversas partes diferentes e informações, por isso queremos que você olhe essa informação abaixo para responder as perguntas a seguir:" — mostra o **claim** da célula ("IF SCTG=1 show PACKAGE Current Lavagem perfeita_claim ..." etc.).
- **VR8B_claim**: "Considerando a nota 5 sendo \"gosto muito\" e 1 \"não gosto nada\", qual nota você daria para essa informação que você acabou de ver?" (1–5)
- **VR8_claim**: "Pensando especificamente nessa informação que você acabou de ver, você diria que ela...?" 1 Chamou muito pouco minha atenção; 2 Chamou um pouco minha atenção; 3 Chamou minha atenção; 4 Chamou muito minha atenção.
- **VR13A**: "Ainda pensando sobre essa informação, qual das descrições abaixo você pensa que pode ser usada para descrever a marca Omo?" (mesma lista de VR13).

---

## 5. Bases e filtros (resumo)
| Pergunta | Base |
|---|---|
| Screener | Total; mulheres 25–55, AB/C, desktop/laptop/tablet, responsável por compra e lavagem, ≥3 máquinas/semana, compra principal sabão em pó |
| BRD / RJC | Marcas conhecidas (CONHCMTO) |
| FRQ_BRAND | Marcas compradas (BRD) — cota de marca |
| Q045/Q45A | Primeiro produto comprado em VR2 |
| Q45B | Só se >1 razão em Q45A |
| VR5 | Não comprou a embalagem teste em VR2 |
| VR7 | Top 2 box em VR6 (cód. 4 ou 5) |
| Demais avaliações | Total da célula (monádico) |

---

## 6. Padrões reutilizáveis
1. **Fluxo clássico de pack test**: screener → funil de marca → **compra em gôndola virtual (comportamento)** → diagnóstico da escolha → **findability cronometrada** → **exposição de 5 s + elementos lembrados** → barreiras → avaliação monádica (PI, valor, gostar, heatmap, atenção, unicidade, brand fit, imagem) → claim isolado.
2. **Células monádicas via dummy de alocação** (SCTG) com n por célula; todas as telas referenciam a imagem por "IF SCTG=x show ...".
3. **Comparação atual × novo** na mesma estrutura de células (Current vs New shelf + pack).
4. **Filtro de dispositivo**: excluir smartphone/e-reader/TV quando há gôndola virtual.
5. **Gôndola obrigatória**: "There must be a purchase, the respondent cannot proceed..." e **gravar a ordem de seleção** (1ª compra é a referência para piping).
6. Instrução de shopping com 3 bullets: disponibilidade real, dinheiro próprio, tempo normal.
7. **Find time** = texto + TIMER_START + tela da gôndola + TIMER_END + pergunta de facilidade (4 pontos).
8. **Exposição tachistoscópica**: mostrar pack por 5 segundos e remover; depois ranking top-3 de elementos lembrados, com a lista filtrada pelos elementos presentes em cada embalagem.
9. **Razões RM → razão principal RU** puxando só as marcadas; pular a RU se só uma razão marcada.
10. **Barreira para não compradores** do produto teste, com "Eu não vi" como código 1 (mede visibilidade).
11. **Frequência só para top 2 box de PI**.
12. **Value for money com preço e gramatura explícitos** no enunciado (escala 5 pontos simétrica "Vale muitíssimo menos ... Vale muitíssimo mais").
13. **Heatmap de likes e dislikes** com opção de escape ("Gostei de tudo"/"Não gostei de nada") seguido de aberta "o que... Por quê?".
14. **Brand fit** com código "Não conheço essa marca".
15. Escalas curtas de 4 pontos sem ponto neutro para atenção/unicidade/interesse; 5 pontos para PI/valor/gostar.
16. **Claim testado isoladamente** após o pack (gostar, atenção, imagem de marca) para separar efeito de design × mensagem.
17. Lista de lembrança (stand out) apresentada **como imagens** e com instrução "Selecione somente aqueles que tem certeza de ter visto".
18. Filtro de coerência de categoria: se compra pó e líquido, perguntar qual mais frequente e encerrar se líquido.
