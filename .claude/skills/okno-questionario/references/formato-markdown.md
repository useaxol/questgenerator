# Formato intermediário do questionário (.md)

O questionário é sempre escrito primeiro neste formato. Ele é lido por `scripts/checar_questionario.py` (checagem
de pulos e linguagem) e por `scripts/gerar_docx.py` (exportação no padrão visual okno). Siga-o à risca.

## 1. Frontmatter (obrigatório)

```yaml
---
job: 183.25.002            # ou "A DEFINIR"
estudo: TRACKING DE MARCAS – CACHAÇA
titulo: QUESTIONÁRIO PRINCIPAL          # vai na caixa teal
tipo: quanti-tracking      # quali-recrutamento | quali-pre-tarefa | quali-roteiro | quanti-adhoc | quanti-teste-produto-recrutamento | quanti-teste-produto | quanti-teste-embalagem | quanti-teste-comunicacao | quanti-tracking | diario-de-uso
modulos: [psm]             # [] | [conjoint, maxdiff, psm]
entrevistas: 1500          # ou "8 GRUPOS" / "20 EPs"
data: FEVEREIRO DE 2026
idioma: pt                 # pt | en
modo: presencial           # presencial | online | cati | capi | clt | hut | gd | ep
painel: PESQUISE+          # opcional (texto no canto do cabeçalho)
classificacao: ""          # opcional, ex.: "ESSITY INTERNAL" (vai no rodapé)
---
```

## 2. Blocos de primeiro nível (`##`)

| Marcador | Uso |
|---|---|
| `## INTRODUÇÃO` | Texto de introdução (parágrafos). |
| `## COTAS` | Uma ou mais tabelas de cotas (ex.: `| A. SEXO (P.1) | Cód |`). |
| `## SEÇÃO: <NOME>` | Início de seção — vira caixa teal no .docx. Seções de filtro devem conter no nome **TRIAGEM**, **FILTRO** ou **RECRUTAMENTO** (o checador exige roteamento em todas as opções delas). |
| `## ENCERRAMENTO` | Texto de encerramento padrão. |
| `## MAPA DE COBERTURA` | Tabela objetivo → perguntas. **Não vai para o .docx.** Tudo após este título é ignorado na exportação. |

## 3. Perguntas (`###`)

```markdown
NOVA TELA:
### P.9 Qual você consome com maior frequência? (RODIZIAR OS TIPOS DE BEBIDAS – ACEITAR SOMENTE RESPOSTAS DE P.8) (RU)
PROGRAMAÇÃO: SE APENAS UMA RESPOSTA EM P.8, TRANSPORTAR PARA P.9 E VÁ PARA P.10
ENTREVISTADOR: MOSTRAR CARTÃO 3
| Opção | Cód | Ação |
|---|---|---|
| Cachaça / aguardente | 3 | CONTINUE |
| Nenhuma destas | 99 | ENCERRE |
```

- Cabeçalho: `### <ID> <enunciado com códigos>`. ID = `P.<n>` / `Q.<n>` (com sufixo opcional `a`, `A`, `_1`) ou
  letra de controle `A.`, `B.`… ou filtro `S1.`.
- Linhas de instrução começam com `PROGRAMAÇÃO:`, `PROGRAMADOR:`, `PN:`, `PROGRAMMING:`, `ENTREVISTADOR:`,
  `INTERVIEWER:`, `PROCESSAMENTO:`, `NOVA TELA`, `NEW SCREEN`, `APLICAR`, `APPLY`, `SOMENTE`, `ONLY`, `SE `, `DEVE`,
  `MUST` — sempre em MAIÚSCULAS.
- Filtro de base vai **antes** do `###` (entre `NOVA TELA:` e a pergunta) ou logo abaixo do `###`.
- Tabela de opções: colunas `Opção | Cód | Ação` (Ação opcional fora da triagem). Use `///` para não codificado.
- Grid de escala: primeira coluna = atributo; demais = pontos da escala com o rótulo no cabeçalho.
  Ex.: `| Atributo | Totalmente insatisfeito(a) | Insatisfeito(a) | … |` e linhas `| Conforto geral | 1 | 2 | 3 | 4 | 5 |`.
- Pergunta aberta: sem tabela; incluir `(ESPONTÂNEO)` e, online, `PROGRAMAÇÃO: MÍNIMO 3 CARACTERES`.

## 4. Tabela combinada (funil de categoria / marcas)

As perguntas do funil são escritas em sequência **sem tabela própria** e a tabela única vem depois da última,
com uma coluna por pergunta:

```markdown
### P.16 Quais marcas de cachaça você conhece, mesmo que só de ouvir falar? (ESPONTÂNEO) (RM) (RODIZIAR MARCAS – SE CITOU TODAS AS MARCAS EM P.16 PULAR A P.17)
### P.17 E quais destas marcas de cachaça você conhece, mesmo que só de ouvir falar? (MOSTRAR TABLET / LER OPÇÕES – RODIZIAR MARCAS) (RM) (APENAS PARA MARCAS NÃO CITADAS EM P.16)
…
| Marca | P.16 | P.17 | P.18 |
|---|---|---|---|
| 51 | 1 | 1 | 1 |
| Nenhuma | /// | 99 | /// |
```

O checador reconhece cabeçalhos `P.x` / `Q.x` nas colunas e atribui os códigos a cada pergunta.

## 5. Formatação inline

- `**negrito**` para ênfase no enunciado (ex.: lojas **FÍSICAS**).
- `[CINZA]` no início de uma célula marca opção-alvo de filtro (vira fundo cinza no .docx): `| [CINZA] TENA | 5 | CONTINUE |`.
- `____` = lacuna preenchida por programação; sempre acompanhada de instrução do que inserir.
- Parágrafos livres (textos de convite, estímulos, conceito) são escritos normalmente e saem como texto.
- Listas `- item` saem como marcadores (útil em roteiros quali).

## 6. Quali (roteiro / pré-tarefa)

Roteiros usam `## SEÇÃO: <BLOCO> (<tempo> min)`, subtítulos `### <n>. <tema>` (sem `P.`), e perguntas em lista
`- `. Instruções ao moderador em linhas `MODERADOR:` (maiúsculas). O checador aplica apenas as regras de linguagem.
