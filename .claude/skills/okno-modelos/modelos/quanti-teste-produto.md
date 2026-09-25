# Modelo — Teste de produto (CLT / HUT)

Referência real: JOB 88.24.010 "SALVE" (Essity/Inco) — recrutamento (1º contato) + avaliação (2º contato), HUT
monádico sequencial com painéis rodiziados. Guia de Estilo §6A.1 e §7.1.

Gera **dois documentos**: `quanti-teste-produto-recrutamento` e `quanti-teste-produto` (principal). Em CLT, os dois
podem ser um único questionário (triagem + avaliação na mesma sessão).

---

## A. RECRUTAMENTO (1º contato)

Título: `QUESTIONÁRIO DE RECRUTAMENTO (1º CONTATO)`

### Cotas
A. SEXO (P.1) · B. REGIÃO (P.3/P.4) · C. IDADE (P.2) · D. CLASSE · E. PAINEL (RODIZIADO) · F. MARCA USUAL.
**Painel** = ordem de avaliação dos produtos por código cego; ex.: `X4Q vs Y3M` 1 · `Y3M vs X4Q` 2 ·
`Z1R vs Y3M` 3 · `Y3M vs Z1R` 4 (todas as ordens para cada par, balanceadas por cota).

### Sequência
1. **Sexo** (não perguntar) → 2. **Idade** (faixas com ENCERRE fora) → 3. **Praça/região** (+ P.4a para região
   metropolitana, `APLICAR P.4a SE CÓD 2 EM P.3`) → 4. **Área de atuação** (incluir saúde/fabricantes/distribuidores
   da categoria).
5. **Funil de categoria** (usa → usa com maior frequência → escolhe e compra), tabela única, filtro composto:
   "PROGRAMAÇÃO: PARA PARTICIPAR, DEVE CITAR CÓD X NA P.6, P.7 E P.8 | CASO CONTRÁRIO ENCERRE".
   `APLICAR P.7 SE MAIS DE UMA RESPOSTA NA P.6 / SE APENAS 1, TRANSFERIR PARA P.7 E PULAR PARA P.8`.
6. **Convite antecipado** (descrição do teste + "Você teria interesse em participar deste estudo? (RU)" Sim CONTINUE ·
   Não ENCERRE) — antes das perguntas de hábito detalhado para não desperdiçar entrevista.
7. **Hábitos filtro** (cada um com CONTINUE/ENCERRE): tempo de uso da categoria · frequência de compra própria ·
   frequência de uso · momento de uso · quantidade por dia · tamanho/versão · motivo principal · intensidade/nível ·
   condição física relevante.
8. **Repertório de marcas** (funil de recrutamento — ver `okno-linguagem/references/funil-de-marcas.md` §4):
   conhece → já usou → costuma usar → usa com maior frequência → usa atualmente → rejeita; filtros "DEVE CITAR MARCA
   EM CINZA… MESMA MARCA NAS DUAS" e "NINGUÉM PODE REJEITAR AS MARCAS TESTADAS".
9. **Versões/variantes** da marca usual (usa → mais usa → usa atualmente) + **pantry check** (foto da embalagem).
10. **Filtros de saúde / sensoriais** (bloco S1–S7 quando alimento/bebida; deficiência visual/auditiva se houver estímulos).
11. **Critério Brasil** (se não estiver no início) com CONTINUE/ENCERRE por classe.
12. **Avaliação do produto habitual** (baseline): gostar (escala presente) + grid de satisfação por dimensão
    (mesmos atributos do principal, `NÃO MOSTRAR ESTA COLUNA` para dimensão, `REPETIR A ESCALA A CADA 4 FRASES`).
13. **Convite** (caixa teal `CONVITE PARA PARTICIPAR DA PESQUISA`): texto com duração, número de produtos, rotina de
    uso, diário, cuidados ("É muito importante que você não mude seus hábitos durante o teste"), sigilo; aceite Sim/Não;
    endereço e dia/horário de entrega.
14. **Termo LGPD** (Sim CONTINUE / Não ENCERRE).

---

## B. PRINCIPAL / AVALIAÇÃO (2º contato — repetir por produto)

Título: `QUESTIONÁRIO DE AVALIAÇÃO (2º CONTATO)`

### 1. Abertura e checagem
- Texto: "A partir de agora, queremos saber a sua opinião sobre o primeiro ____ que você recebeu em casa para usar."
  `PROGRAMAÇÃO: NA AVALIAÇÃO DO 2º PRODUTO, TROCAR O TEXTO: "…sobre o segundo ____…"`
- **Código do produto**: "A embalagem dos produtos que entregamos na sua casa estava identificada por um código.
  Qual era o código do primeiro produto que você experimentou? (RU)"
  `PROGRAMAÇÃO: O CÓDIGO DEVE SER O DO 1º PRODUTO DO PAINEL AO QUAL O RESPONDENTE FOI ALOCADO; CASO CONTRÁRIO, ENCERRE E INFORME IMEDIATAMENTE A EQUIPE DE CAMPO`
  + mensagem ao respondente "Por favor, verifique se o código selecionado está correto".
- **Quantidade usada** (1 · 2 · 3 · 4 · 5 ou mais) → `SOMENTE PARA CÓDS 1 A 3`: "Você pretende continuar usando
  este produto nos próximos dias?" Sim → MENSAGEM "use mais algumas unidades… e responda esta pesquisa em 2 dias" →
  `SOMENTE PARA CÓD 2`: "Por que você usou tão poucas unidades…?" problema com o produto → CONTINUE ·
  questões pessoais → ENCERRE.

### 2. Avaliação global (ordem fixa)
1. Gostar/desgostar (escala 1)
2. "Do que você **mais** gostou neste produto? O que mais? (ESPONTÂNEO) (PROGRAMAÇÃO: MÍNIMO 3 CARACTERES)"
3. "E do que você **menos** gostou…? O que mais? (ESPONTÂNEO)"
4. Qualidade geral (escala 5)
5. Intenção de compra (escala 2)
6. Comparação vs. habitual (escala 7)
7. Substituição do habitual (escala 8)
8. Diferenciação (escala 9)

### 3. Avaliação por dimensão (uma seção por dimensão do produto)
Para cada dimensão (ex.: DIMENSÕES E AJUSTE · CONFORTO E CONTATO COM A PELE · SEGURANÇA E ABSORÇÃO — adapte às
dimensões da categoria):
- Grid de satisfação `(RU POR ATRIBUTO) (ATRIBUTOS EM RODÍZIO)`;
- **JAR** dos atributos sensoriais/de ajuste ("NOVA TELA PARA CADA BLOCO, MANTENDO A PERGUNTA INICIAL FIXA");
- Escalas diagnósticas descritivas dos atributos-chave;
- Ocorrências com pulo: "Este produto ____ durante o teste? Sim 1 CONTINUE · Não 2 PULE PARA P.X" →
  `NOVA TELA – SOMENTE PARA CÓD 1 NA P.Y`: "Onde…? (RM)".

### 4. Concordância com frases (claims do produto) — escala 4, RODIZIAR

### 5. Preço
- PSM (módulo `modulos/psm.md`) se pedido;
- Intenção de compra com preço ("…pelo preço de R$ ___ (PROGRAMAÇÃO: INSERIR PREÇO CONFORME TABELA, SEGUNDO O PRODUTO TESTADO)…");
- Intenção por marca (branded vs blind): "Qual seria a sua intenção de compra deste produto se ele fosse da marca ____?
  (PROGRAMAÇÃO: RODIZIAR MARCAS – APLICAR PARA CADA MARCA SEPARADAMENTE)".

### 6. Repetição
"PROGRAMAÇÃO: REPETIR TODO O QUESTIONÁRIO DE AVALIAÇÃO DO 1º PRODUTO PARA O 2º PRODUTO" (título:
`QUESTIONÁRIO DE AVALIAÇÃO DO 2º PRODUTO TESTADO (APÓS X DIAS DE USO)`).

### 7. Comparação entre produtos (só após o último)
- Preferência: "Agora que você experimentou os dois ____, qual você prefere? (RU)" Código ___, o PRIMEIRO 1 · o SEGUNDO 2.
- "Por que você prefere ____ (RESPOSTA DA P.X)? Escreva com suas palavras… (MÍNIMO 3 CARACTERES)".
- Preferência por aspecto (grid aspectos × produto, RODIZIAR ASPECTOS).
- Escolha com preço: "Se você fosse comprar ____ e encontrasse estes 2 produtos… por estes preços, qual compraria? (RU)".
- "Você notou alguma diferença entre os dois produtos? Sim CONTINUE · Não PULE PARA P.X" → "Qual diferença…?".
- Escolha vs. habitual com preço (texto condicional por painel).

### 8. Blocos opcionais (se o briefing pedir)
Conceito (ler descrição → gostar → intenção com preço → adequação ao produto) · Embalagem (ver
`quanti-teste-embalagem.md`) · Nomes (1º e 2º mais adequado) · Simulação de gôndola (escolha entre N produtos com
preços, 3 rodadas) · Selos (associação selo × frase, RM por frase; impacto na marca).

### 9. Encerramento
"Nossa pesquisa termina aqui. Muito obrigado pela sua participação."

---

## Objetivos típicos → blocos
| Objetivo de briefing | Bloco / KPI |
|---|---|
| Aprovação do produto / go-no go | Gostar (T2B), intenção (T2B), comparação vs. habitual |
| Paridade/superioridade vs. concorrente | Monádico sequencial + preferência + preferência por aspecto |
| Otimização de atributos | Grid de satisfação + JAR (penalty) |
| Preço | PSM + intenção com preço + escolha com preço |
| Força de marca | Intenção por marca (blind vs. branded) |
