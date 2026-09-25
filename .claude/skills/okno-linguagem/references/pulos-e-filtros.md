# Pulos, filtros, pipes e transferências — padrão okno

Os questionários okno controlam o fluxo com **seis mecanismos**. Todo questionário gerado deve usar exatamente esta
gramática, porque o script `scripts/checar_questionario.py` e o analista sênior a validam.

## 1. Roteamento na própria opção (coluna de ação)

Usado em **toda pergunta de filtro**. A terceira coluna da tabela de opções diz o que acontece.

```
Você usa fralda descartável durante o dia ou à noite? (RU)
| Apenas durante o dia | 1 | ENCERRE |
| Apenas à noite       | 2 | ENCERRE |
| Dia e noite          | 3 | CONTINUE |
```

- Célula vazia abaixo de um roteamento = **mesmo roteamento da linha de cima** (convenção dos docs okno). No formato
  gerado pela IA, **repita o roteamento em todas as linhas** — é mais seguro para programação e revisão.
- `///` na coluna de código = opção não codificada (faixa de idade fora do público).
- Pulo condicional: `| Não | 2 | PULE PARA P.52 |`.

## 2. Filtro de base (quem responde a pergunta)

Linha em MAIÚSCULAS **imediatamente antes** da pergunta:

| Padrão | Exemplo literal okno |
|---|---|
| `APLICAR P.X SE CÓD Y EM P.Z` | "APPLY Q.4 IF CODE 1 IN Q.3" |
| `NOVA TELA – SOMENTE PARA CÓD Y NA P.Z` | "NEW SCREEN – ONLY FOR CODE 1 IN Q.50" |
| `SOMENTE SE DER NOTA CÓD 0 A 8 PARA MARCA 51 EM P.29` | Tracking Cachaça |
| `PN: APPLY Q22 TO Q24 IF ANY CODE/BRAND IS SELECTED AS CODE 1 OR 3 IN Q21` | Filtro de bloco (Varejo) |
| `[APPLY IF Q18 = 1 TO 22]` | Início do enunciado (Varejo) |

**Regra de coerência**: se P.50 tem `Não → PULE PARA P.52`, então P.51 **precisa** ter `SOMENTE PARA CÓD 1 NA P.50`.
Pulo e filtro de base são as duas faces da mesma regra e devem bater.

## 3. Pipe — aceitar apenas menções anteriores

- `(ACEITAR APENAS MENÇÕES DE P.18)` · `(ACEITAR SOMENTE RESPOSTAS DE P.7)`
- Exclusão: `(ACEITAR APENAS MENÇÕES DE P.16/P.17 EXCETO CITADAS EM P.21)` ·
  `(ACEITAR SOMENTE RESPOSTAS DIFERENTES DE P.8, P.9 E P.10)`
- Online: `RANDOMIZE – PIPE CODES SELECTED IN Q13 + CODE 99` ·
  `PIPE CODES SELECTED IN Q13 AND NOT SELECTED IN Q15, Q16 OR Q17`
- EN: `SHOW ONLY BRANDS THE RESPONDENT KNOWS IN Q.19` · `SHOW ONLY ANSWERS MENTIONED IN Q.19 BUT NOT MENTIONED IN Q.21`

O pipe **sempre aponta para uma pergunta anterior**.

## 4. Transferência automática (resposta única derivada)

Quando a pergunta RU vem de uma RM e só houve uma menção, não se pergunta:

- "(SE APENAS UMA RESPOSTA EM P.8, TRANSPORTAR PARA P.9 E VÁ PARA P.10)"
- "IF ONLY 1 BRAND IN Q.21, TRANSFER IT TO Q.22 AND SKIP TO Q.23"
- "PN: IF ONLY 1 OPTION IS SELECTED IN Q31, AUTO PUNCH THIS CODE IN Q32 AND SKIP Q32"
- Exclusão total: "(SE EM P.21 CITOU TODAS AS MARCAS DE P.16/P.17, ASSINALAR AUTOMATICAMENTE 'NENHUMA' EM P.26 E VÁ PARA P.27)"
- Espontâneo → estimulado: "(SE CITOU TODAS AS MARCAS EM P.16 PULAR A P.17)" +
  "PROCESSAMENTO: TRANSFERIR MARCAS CITADAS EM P.16 PARA P.17"
- Chefe de família: "(SE ENTREVISTADO NÃO FOR CHEFE DE FAMÍLIA, PERGUNTE. CASO CONTRÁRIO, TRANSFIRA RESPOSTA ANTERIOR PARA P.C)"

## 5. Filtro composto (checagem após um bloco)

Linha em MAIÚSCULAS **depois** da(s) pergunta(s) que definem a elegibilidade:

- "DEVE CITAR CACHAÇA (CÓD 3) EM P.8, CASO CONTRÁRIO ENCERRE"
- "PROGRAMMING: TO PARTICIPATE, MUST MENTION CODE 7 IN Q.6, Q.7 AND Q.8 | OTHERWISE TERMINATE"
- "MUST MENTION ONE OF THE BRANDS IN GRAY (CODE 4 OR 5) IN Q.22 AND Q.23 AND THE SAME BRAND MUST BE MENTIONED IN BOTH QUESTIONS. OTHERWISE, TERMINATE"
- "NOBODY CAN REJECT NEITHER TENA NOR PLENITUD (CODES 4 AND 5) IN Q.24. OTHERWISE, TERMINATE"
- "SE NÃO CONHECER NA P16/17 NENHUMA DAS 7 MARCAS DA PRAÇA, ENCERRE"
- "PN: TERMINATE IF CODE 99 IS SELECTED IN Q23 AND Q26"

Marcas/códigos-alvo de filtro são sinalizados **em cinza** na tabela (no .docx) e citados por código na instrução.

## 6. Variáveis ocultas e checagens de qualidade (online)

- `PN: PUNCH HIDE 'CANAL'` com regra por linha (ex.: SHOPPER ONLINE se Q23 = 99 E Q26 = 1 A 22).
- `PN: CREATE HIDE 'Q24CHECK'` somando respostas.
- `SPEEDER CHECK: AFTER Q21` · `STRAIGHT LINE: NOT APPLY` · perguntas de atenção (`PROG RH1`).
- Checagem de código de produto (teste de produto): "PROGRAMAÇÃO: O CÓDIGO DEVE SER O DO 1º PRODUTO DO PAINEL AO
  QUAL O RESPONDENTE FOI ALOCADO; CASO CONTRÁRIO, ENCERRE E INFORME IMEDIATAMENTE A EQUIPE DE CAMPO".

## 7. Rodízio

- Marcas: `(RODIZIAR MARCAS)` em **todas** as perguntas do funil de marcas.
- Atributos: `(APRESENTAR ATRIBUTOS EM RODÍZIO)` / `RODIZIAR ATRIBUTOS`; em grids por dimensão, rodiziar dentro do
  bloco e manter o bloco em tela própria.
- Rodízio casado: "PN: RANDOMIZE Q11 AND Q12 ACCORDING TO THE ORDER OF Q9 AND Q10".
- Estímulos monádicos sequenciais: "RODIZIAR VERSÕES DE EMBALAGEM E PARA CADA UMA APLICAR O BLOCO P.77 A P.82".
- Itens fixos: `Outro (FIXO – no fim)`, `Nenhum (EXCLUSIVA / FIXA)`, `Outro TENA (FIXO no fim das marcas TENA)`.

## 8. Repetição de blocos

- "PROGRAMAÇÃO: REPETIR TODO O QUESTIONÁRIO DE AVALIAÇÃO DO 1º PRODUTO PARA O 2º PRODUTO" + troca de texto
  ("PROGRAMAÇÃO: NA AVALIAÇÃO DO 2º PRODUTO, TROCAR O TEXTO: …").
- "PERGUNTAR PARA CADA MARCA CITADA EM P.21 – RODIZIAR MARCAS" + `(RU POR MARCA AVALIADA)`.

## 9. Checklist de consistência de pulos (usado pelo analista sênior)

1. Todo `PULE PARA P.X` aponta para uma pergunta **existente** e **posterior**.
2. Toda pergunta pulada por alguém tem filtro de base explícito coerente com o pulo.
3. Todo pipe (`ACEITAR APENAS MENÇÕES DE P.X`) aponta para pergunta **anterior**, da mesma lista de códigos.
4. Os códigos de uma mesma lista (marcas, tipos, atributos) são **idênticos** em todas as perguntas que a usam.
5. Nenhuma pergunta fica órfã (sem ninguém que chegue a ela) e nenhum caminho termina sem ENCERRE ou encerramento.
6. Filtros de triagem cobrem todas as opções (nenhuma opção sem roteamento).
7. As cotas do cabeçalho apontam para as perguntas corretas (ex.: `A. SEXO (P.1)`) e os códigos batem.
8. Transferências automáticas estão previstas para toda RU derivada de RM.
9. Filtros compostos (`DEVE CITAR…`) são coerentes com o público do briefing.
10. Não sobrou placeholder (`CONTINUAR OU ENCERRAR`, `[INSERIR…]`, `____` sem instrução do que inserir,
    linhas `MARCA 1…N` sem tabela de marcas por praça + instrução de pipe).
11. Todo nível de funil/lista que pode ficar vazio tem `Nenhuma` (99) ou pulo explícito; nenhuma RU com base vazia.
12. Toda coluna de cota tem pergunta de origem, com rótulos e códigos idênticos.
