# Blocos fixos okno

Ordem obrigatória na triagem (Guia de Estilo §9.1): **Critério Brasil → Sexo → Idade → Filtro de área de atuação**.
Filtros de categoria / produto vêm logo depois. Em recrutamento de teste de produto a okno às vezes coloca o
Critério Brasil no fim da triagem (Inco) — só faça isso se o briefing pedir; o padrão é no início.

Cada bloco termina com a instrução de transferência para o controle de cotas:
`PROGRAMAÇÃO: TRANSFERIR PARA P.<LETRA> DO CONTROLE DE COTAS`.

---

## 1. Critério Brasil (classificação socioeconômica)

> ⚠️ **Versão**: o Guia de Estilo v1.0 manda usar o nome "Novo Critério Brasil 2026", mas a tabela de pontos que ele
> traz é a do critério 2015–2024 (usada no Teste Inco, 2025). O tracking de cachaça (fev/2026) já usa a versão
> 2026, com outros pesos e 7 classes. **Pergunte na descoberta qual versão o cliente/instituto está usando.** Se a
> resposta for "Não tenho essa informação", use a **Versão 2026** e registre isso na ficha do projeto como
> `[PROPOSTO PELA IA — VALIDAR]`. Sempre confira os pesos com a publicação da ABEP antes do campo.

Texto de introdução (PT):
"(DADOS DE CLASSIFICAÇÃO ECONÔMICA – NOVO CRITÉRIO BRASIL 2026) Farei algumas perguntas sobre itens do domicílio para
classificação socioeconômica. Por favor, responda considerando apenas itens que estão funcionando ou que você tenha
intenção de consertar nos próximos 6 meses. Na sua casa tem..."

EN: "I will now ask some questions about household items for socioeconomic classification. Please answer considering
only items that are working or that you intend to repair in the next 6 months. Do you have at home..."

### 1.1 Versão 2026 (Tracking Cachaça 183.25.002, fev/2026)

**A. Posse de itens (Não tem / Tem)**

| Item | Não tem | Tem |
|---|---|---|
| Empregada doméstica ou outros empregados da casa que trabalhem pelo menos 5 dias na semana? | 0 | 5 |
| Lava-louça? | 0 | 5 |
| Máquina de lavar roupa que faça todo o processo de lavagem, do molho até centrifugação, sem considerar o tipo "tanquinho"? | 0 | 6 |
| Micro-ondas? | 0 | 7 |
| Água encanada (de uma rede de distribuição)? | 0 | 10 |

**A (cont.). Quantidade**

| Item | 0 | 1 | 2 | 3 | 4+ |
|---|---|---|---|---|---|
| Banheiros, incluindo o de empregada? (Se sim) Quantos? | 0 | 9 | 15 | 19 | 20 |
| Automóveis de passeio? Não considere caminhões e veículos usados como táxi ou kombis utilizadas para uso profissional. (Se sim) Quantos? | 0 | 4 | 8 | 10 | 11 |
| Microcomputador? (Se sim) Quantos? | 0 | 6 | 11 | 13 | 15 |
| Geladeira, independentemente do número de portas, mas excluindo equipamentos que sejam apenas freezer? (Se sim) Quantas? | 0 | 6 | 10 | 12 | 13 |

**B. Até que ano de escola o chefe de família cursou? Considere a última série concluída.**
**C. (OPCIONAL — PERFIL; NÃO PONTUA) (SE ENTREVISTADO NÃO FOR CHEFE DE FAMÍLIA, PERGUNTE. CASO CONTRÁRIO, TRANSFIRA RESPOSTA ANTERIOR PARA P.C) Até que ano de escola você cursou?**

| Nomenclatura antiga | Nomenclatura atual | Chefe da família |
|---|---|---|
| Analfabeto / Sem instrução | Analfabeto / sem instrução | 0 |
| Primário incompleto / Primário completo / Ginásio incompleto | Ensino fundamental incompleto | 3 |
| Ginásio completo | Fundamental completo (até 9º ano) | 4 |
| Colegial incompleto | Ensino médio incompleto | 5 |
| Colegial completo | Ensino médio completo | 6 |
| Superior incompleto | Ensino superior incompleto | 6 |
| Superior completo | Ensino superior completo | 8 |

**D. Classificação social. ENTREVISTADOR: SOME PONTOS A + B**

| Classe | Pontos | Cód |
|---|---|---|
| A | 73 a 100 | 1 |
| B1 | 66 a 72 | 2 |
| B2 | 55 a 65 | 3 |
| C1 | 46 a 54 | 4 |
| C2 | 35 a 45 | 5 |
| DE+ | 11 a 34 | 6 |
| DE- | 0 a 10 | 7 |

Cada classe recebe `CONTINUE` ou `ENCERRE` conforme o público do briefing.
`PROGRAMAÇÃO: TRANSFIRA PARA P.C DO CONTROLE DE COTAS`

### 1.2 Versão 2015–2024 (Guia de Estilo §4 / Teste Inco 2025)

Itens com quantidade (0 / 1 / 2 / 3 / 4+):

| Item | 0 | 1 | 2 | 3 | 4+ |
|---|---|---|---|---|---|
| Banheiros | 0 | 3 | 7 | 10 | 14 |
| Trabalhadores mensalistas (pelo menos 5 dias por semana) | 0 | 3 | 7 | 10 | 13 |
| Automóveis de passeio exclusivamente para uso particular | 0 | 3 | 5 | 8 | 11 |
| Microcomputadores (desconsiderar tablets, palms ou smartphones) | 0 | 3 | 6 | 8 | 11 |
| Lava-louças | 0 | 3 | 6 | 6 | 6 |
| Geladeiras | 0 | 2 | 3 | 5 | 5 |
| Freezers independentes ou parte da geladeira duplex | 0 | 2 | 4 | 6 | 6 |
| Máquinas de lavar roupa, excluindo tanquinho | 0 | 2 | 4 | 6 | 6 |
| DVD (qualquer dispositivo que leia DVD, desconsiderando o de automóvel) | 0 | 1 | 3 | 4 | 6 |
| Fornos de micro-ondas | 0 | 2 | 4 | 4 | 4 |
| Motocicletas (desconsiderar uso exclusivamente profissional) | 0 | 1 | 3 | 3 | 3 |
| Secadoras de roupa (considerando lava e seca) | 0 | 2 | 2 | 2 | 2 |

Escolaridade do chefe: Analfabeto / Fund. I incompleto = 0 · Fund. I completo / Fund. II incompleto = 1 ·
Fund. II completo / Médio incompleto = 2 · Médio completo / Superior incompleto = 4 · Superior completo = 7.

Serviços públicos: Água encanada Sim = 4 · **Rua pavimentada** Sim = 2.
(O Guia v1.0 traz "Ensino superior completo 2 pts" nesta tabela — é erro de digitação; o correto, como no
questionário Inco, é **rua pavimentada**.)

Classes: A 45–100 · B1 38–44 · B2 29–37 · C1 23–28 · C2 17–22 · DE 0–16.
`ENTREVISTADOR: SOME PONTOS G + H + J + K`

---

## 2. Sexo — não perguntar, observar (RU)

`SEXO: NÃO PERGUNTE (RU)` · EN: `INTERVIEWER, WRITE DOWN THE RESPONDENT'S GENDER, WITHOUT ASKING (SC)`
`PROGRAMAÇÃO: TRANSFIRA PARA P.A DO CONTROLE DE COTAS`

| Feminino | 1 | CONTINUE/ENCERRE |
|---|---|---|
| Masculino | 2 | CONTINUE/ENCERRE |
| Outro | 3 | … |
| Prefiro não dizer | 4 | … |

Online (autodeclarado, padrão Varejo): "Você se identifica como: [SS]" Mulher 1 · Homem 2 · De outra forma 3 ·
Prefiro não informar 4 → `PUNCH HIDE 'GENDER_QUOTA'`.

## 3. Idade — espontâneo (RU)

"Qual sua idade? (ESPONTÂNEO) (RU)"
`ENTREVISTADOR: ANOTE IDADE EXATA E FAIXA`
`PROGRAMAÇÃO: TRANSFIRA PARA P.B DO CONTROLE DE COTAS`

| Anote: \|__\|__\| | | |
|---|---|---|
| Menos de [MÍNIMO] anos | /// | ENCERRE |
| [Faixa 1] | 1 | CONTINUE |
| [Faixa n] | n | CONTINUE |
| Acima de [MÁXIMO] anos | /// | ENCERRE |

Faixas padrão: 16–24 · 25–34 · 35–44 · 45–54 · 55+ (ajustar ao público do briefing).
Online: `RANGE 1 TO 99` · `TERMINATE IF <18 OR >60` · `PUNCH HIDE 'C.IDADE'`.

## 4. Filtro de área de atuação (RM) — sempre a última da triagem demográfica

"Atualmente, você ou alguém na sua casa trabalha em... (LEIA ALTERNATIVAS) (RM)"

| Área | Cód | Ação |
|---|---|---|
| Agência de propaganda ou publicidade | 1 | ENCERRE |
| Instituto de pesquisa de mercado | 2 | ENCERRE |
| Jornal, revista, TV ou rádio | 3 | ENCERRE |
| Empresa na área de Marketing | 4 | ENCERRE |
| [PERSONALIZAR: fabricantes da categoria do estudo] | 5 | ENCERRE |
| [PERSONALIZAR: distribuidores / varejistas da categoria] | 6 | ENCERRE |
| Nenhum destes lugares (EXCLUSIVA) | 99 | CONTINUE |

Exemplos reais de personalização: "Distribuidores ou comércios de bebidas alcoólicas, como bares, lanchonetes,
restaurantes, supermercados" + "Fabricantes de bebidas alcoólicas" · "Empresas de saúde, clínicas ou hospitais" +
"Fabricantes de produtos de higiene pessoal" + "Distribuidores de produtos de higiene pessoal, como supermercados e
farmácias" · "Empresas que fabricam roupas, calçados e acessórios" + "Lojas que vendem roupas, calçados e acessórios".

## 5. Outros filtros recorrentes

- **Participação recente em pesquisa** (quali e recrutamento): "Você participou de alguma pesquisa de mercado,
  grupo de discussão ou entrevista nos últimos 6 meses? (RU)" Sim → ENCERRE · Não → CONTINUE.
- **Deficiência visual/auditiva** (quando há estímulos): "Neste estudo vamos apresentar alguns materiais para
  avaliação visual e auditiva. Você tem alguma deficiência visual ou auditiva? (ESPONTÂNEO) (RU)" Sim → ENCERRE.
- **Estado civil** (perfil, sem filtro): "Qual seu estado civil atual? (LEIA OPÇÕES) (RU)" Solteiro 1 · Casado / mora
  junto 2 · Separado / divorciado 3 · Viúvo 4.
- **Praça / região**: "Onde você mora? (ESPONTÂNEO) (RU)" com cidade / região metropolitana / outra → ENCERRE e sub-pergunta
  de bairro/região (P.4a) aplicada apenas ao código correspondente.
- **Raça/cor** (online): "Com qual classificação racial você se identifica? [SS]" Amarelo/a · Branco/a · Indígena ·
  Pardo/a · Preto/a · Outra · Não sei dizer · Prefiro não responder.

## 6. Bloco fixo de teste de produto (CLT/HUT) — S1 a S7

Aplicar quando o produto é ingerível/aplicável. Cada opção recebe CONTINUE ou ENCERRE **definidos no projeto**
(o placeholder `CONTINUAR OU ENCERRAR` nunca pode ficar no questionário final).

- S1. Sobre o consumo de produtos industrializados, você diria que: (RU) — "Eles são parte da minha rotina e consumo
  regularmente" 1 · "Evito o consumo, mas consumo de vez em quando" 2 · "Rejeito totalmente o consumo de produtos
  industrializados" 3.
- S2. Você tem alergia a algum dos grupos, alimentos ou princípios abaixo? (RODIZIAR) (RM) — Cereais com glúten 1 ·
  Leguminosas (soja, amendoim) 2 · Oleaginosas e castanhas 3 · Peixes e frutos do mar 4 · Ovos 5 · Lactose / proteína
  do leite 6 · Látex natural 7 · Fenilalanina (PKU) 8 · Corantes artificiais (ex.: tartrazina E102) 9 · Não tenho
  alergia alimentar 99 (EXCLUSIVA / FIXA). `PROGRAMAÇÃO: ENCERRAR SE CÓDS __ A __ DE ACORDO COM OS PARÂMETROS DO ESTUDO`.
- S3. Você está grávida ou amamentando atualmente? (RU) — Sim 1 · Não 2.
- S4. Você já fez cirurgia bariátrica? (RU) — Sim 1 · Não 2.
- S5. Atualmente você faz uso ou fez uso nos últimos 3 meses de canetas emagrecedoras ou algum medicamento injetável
  utilizado para emagrecimento ou controle de peso, como Ozempic, Wegovy, Mounjaro ou similares? (RU) — Sim 1 · Não 2.
- S6. Neste momento, você está com ou suspeita de gripe, resfriado, ou algum problema que afete seu paladar ou olfato?
  (RU) — Sim 1 · Não 2.
- S7. Considerando as últimas 2 horas, você diria que…? (RM) — Fumou cigarro tradicional ou eletrônico 1 · Consumiu
  café 2 · Escovou os dentes 3 · Consumiu bala ou chiclete de menta/anis/hortelã ou refrescante 4 · Não pratiquei
  nenhuma das atividades… 99 (EXCLUSIVA / FIXA).

## 7. Aceite LGPD / termo de confidencialidade (recrutamentos)

"Gostaria de reforçar que suas respostas serão mantidas em sigilo, sem identificação dos respondentes… Ao concordar
com este termo, você confirma que forneceu informações corretas nas perguntas de seleção e se compromete a não
repassar as informações recebidas e discutidas a nenhuma agência ou entidade concorrente do produto ou serviço
estudado. Você confirma que concorda com estes termos? (RU)" Sim 1 CONTINUE · Não 2 ENCERRE.

## 8. Aceite de compartilhamento de contato com o cliente (fim do questionário, se pedido)

"O cliente que contratou esta pesquisa é a ____, fabricante de ____. Você aceita que os seus contatos (nome, telefone,
e-mail) sejam compartilhados com a ____ somente com a finalidade de que eles entrem em contato com você para realizar
outras pesquisas? (RU)" Aceito 1 · Não aceito 2.
