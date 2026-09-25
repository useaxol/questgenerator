---
name: okno-linguagem
description: Linguagem, convenções e padrões de redação de questionários da okno Núcleo de Estudos (códigos RU/RM, instruções de PROGRAMAÇÃO, NOVA TELA, escalas de 5 pontos, blocos fixos, Critério Brasil, funil de marcas, pulos e filtros). Use SEMPRE que for escrever, revisar ou corrigir qualquer pergunta, instrução ou bloco de questionário okno — quali ou quanti.
---

# Linguagem okno — questionários

Esta skill é a **fonte de verdade de estilo**. Ela consolida o *Guia de Estilo okno v1.0 (2026)*
e os padrões observados nos questionários reais da okno (Tracking Cachaça 183.25.002,
Monitoramento de Marca Varejo 267.25.006, Teste de Produto Inco 88.24.010 — recrutamento e principal).

Antes de redigir, leia as referências conforme a necessidade:

| Preciso de… | Leia |
|---|---|
| Cabeçalho, introdução, cotas, encerramento, rodapé | `references/cabecalho-e-encerramento.md` |
| Escalas padrão (5 pontos, NPS, JAR, comparação, diagnósticas) | `references/escalas.md` |
| Blocos fixos de triagem (Critério Brasil, sexo, idade, área de atuação, filtros de teste de produto) | `references/blocos-fixos.md` |
| Pulos, filtros, pipes, transferências, ENCERRE/CONTINUE | `references/pulos-e-filtros.md` |
| Funil de categoria e **funil/pirâmide de marcas** | `references/funil-de-marcas.md` |

## 1. Princípios de redação (sempre)

1. **Pergunta ao respondente em linguagem natural, curta e coloquial**, em 2ª pessoa ("você").
   Ex.: "Quais marcas de cachaça você conhece, mesmo que só de ouvir falar?"
2. **Tudo o que não é lido ao respondente vai em MAIÚSCULAS** e entre parênteses ou precedido de rótulo:
   `PROGRAMAÇÃO:` / `PROGRAMADOR:` / `PN:` (online) · `ENTREVISTADOR:` · `PROCESSAMENTO:`.
3. **Todo código de tipo de resposta aparece ao final do enunciado**: `(RU)`, `(RM)`, `(ESPONTÂNEO)`,
   `(LEIA ALTERNATIVAS)`, `(MOSTRAR TABLET / LER OPÇÕES)`, `(RU POR LINHA)`, `(RODIZIAR)`.
4. **Toda opção de triagem tem roteamento** (`CONTINUE`, `ENCERRE`, `PULE PARA P.X`). Opções que não se aplicam a
   uma coluna levam `///`.
5. **`NOVA TELA:`** em linha própria, antes de cada pergunta/tela (obrigatório em estudos online/CAPI).
6. **Numeração sequencial** `P.1, P.2…` (PT) ou `Q.1, Q.2…` (EN). Sub-perguntas derivadas: `P.4a`, `P.64A…P.64D`.
   Perguntas de controle de cotas/classificação usam letras: `A.`, `B.`, `C.`…
7. **O texto da introdução menciona o tema geral, nunca o cliente**. Perguntas específicas sobre a marca-cliente
   (follow-ups de NPS, aprofundamentos) são permitidas **depois** do funil, quando ela já apareceu entre as demais
   marcas; o que não pode é identificá-la como contratante antes do fim (aceite de compartilhamento de contato).
8. **Ancoragem de "Outro" e "Nenhum"**: `Outro (especifique)` e `Nenhum destes` são sempre **FIXOS** no fim da
   lista; `Nenhum` é **EXCLUSIVO** e usa código **99** (`98` = Não sei / Não lembro).
9. **Escalas são sempre as da `references/escalas.md`**, 5 pontos com todos os pontos nomeados, do negativo (1)
   para o positivo (5). NPS 0–10. Não inventar escala sem justificativa do briefing.
10. **Abertas**: indicar `(ESPONTÂNEO)`, `O que mais?` no enunciado, e para online `(PROGRAMAÇÃO: MÍNIMO 3 CARACTERES)`.
    Para razões: `(EXPLORE AS RESPOSTAS) (DEVEMOS TER PELO MENOS 2 RAZÕES)`.
11. **Referência a respostas anteriores usa `____ (LER MARCA / RESPOSTA DA P.X)`** no enunciado; online:
    `[PIPE Qx BRAND TEXT]`.
12. **Um conceito por pergunta**. Nada de perguntas duplas ("gostou e compraria?").
13. **Tempo verbal coerente com o recorte**: "nos últimos 6 meses", "no último ano", "atualmente", "costuma".
14. **Linguagem inclusiva e neutra**: "satisfeito(a)", "Outro", "Prefiro não dizer".

## 2. Tabela de códigos de resposta

| PT | EN | Online (programação) | Uso |
|---|---|---|---|
| (RU) | (SC) | [SS] | Resposta única |
| (RM) | (MC) | [MS] | Resposta múltipla |
| (ESPONTÂNEO) | (SPONTANEOUS) | [OE] / [OEN] numérica | Não mostrar opções |
| (LEIA ALTERNATIVAS) | (READ THE ALTERNATIVES) | — | Ler opções |
| (MOSTRAR TABLET / LER OPÇÕES) | (SHOW TABLET / READ OPTIONS) | — | Mostrar e ler |
| (RU POR LINHA) | (SC PER ATTRIBUTE) | [TT1] / CARROUSSEL | Grid de escala |
| (RM POR LINHA) | (MC PER ROW) | [TT3 – MS PER ROW] | Grid de associação |
| (RODIZIAR) | (RANDOMIZE) | RANDOMIZE | Rodízio |
| (FIXO) | (FIXED) | [ANCHOR] | Item fixo |
| (EXCLUSIVA) | (EXCLUSIVE) | [EXCLUSIVE] | Anula as demais |

Escolha **um registro** por questionário: presencial/CATI/CAPI em PT → `(RU)/(RM)` + `PROGRAMAÇÃO:`;
online em plataforma → pode usar `[SS]/[MS]` + `PN:` (padrão Varejo). Não misturar os dois registros.

## 3. Roteamento — vocabulário controlado

| PT | EN | Significado |
|---|---|---|
| CONTINUE | CONTINUE | Segue para a próxima pergunta |
| ENCERRE | TERMINATE | Encerra a entrevista (filtro) |
| PULE PARA P.X | SKIP TO Q.X | Salta perguntas |
| VÁ PARA P.X | GO TO Q.X | Idem (usado após transferência) |
| APLICAR P.X SE CÓD Y EM P.Z / SOMENTE PARA CÓD Y EM P.Z | APPLY Q.X IF CODE Y IN Q.Z | Filtro de base |
| ACEITAR APENAS MENÇÕES DE P.X | SHOW ONLY ANSWERS FROM Q.X / PIPE CODES SELECTED IN QX | Pipe |
| TRANSFERIR / TRANSPORTAR PARA P.X | TRANSFER / AUTO PUNCH | Preenchimento automático |
| CONTINUAR OU ENCERRAR | — | Placeholder em bloco fixo a ser definido pelo estudo (**nunca pode ficar no questionário final**) |

Detalhes e exemplos literais: `references/pulos-e-filtros.md`.

## 4. Ordem padrão do questionário quanti

1. Cabeçalho (JOB nº, estudo, N entrevistas, data, campos do respondente)
2. Tabela Entrevistador / Crítico / Verificador (CPF, DATA) + Voltas de processamento / Código do codificador
3. Título (caixa com fundo teal) — ex.: `QUESTIONÁRIO DE RECRUTAMENTO (1º CONTATO)`
4. Introdução (maiúsculas, LGPD, gravação) + tabela de COTAS (A. SEXO, B. IDADE, C. CL. SOCIAL, D. PRAÇA…)
5. **Triagem — blocos fixos**: Critério Brasil → Sexo → Idade → Filtro de área de atuação
   (+ filtros de categoria e, em teste de produto, os filtros S1–S7)
6. Seções específicas do estudo (título de seção em caixa alta: `CONSUMO DE …`, `PIRÂMIDE DE MARCAS DE …`,
   `NPS E AVALIAÇÃO DAS MARCAS`, `AVALIAÇÃO DO PRODUTO HABITUAL`…)
7. Encerramento padrão
8. Tabela `VOLTAS DE CAMPO | COMENTÁRIOS DE CAMPO`
9. Rodapé okno (9 pt, centralizado)

## 5. Checklist rápido de linguagem (auto-verificação antes de entregar)

- [ ] Toda instrução não lida está em MAIÚSCULAS e rotulada
- [ ] Toda pergunta tem código de tipo de resposta
- [ ] Toda opção de filtro tem roteamento; nenhum `CONTINUAR OU ENCERRAR` sobrou
- [ ] Escalas idênticas às da referência (rótulos e códigos)
- [ ] `Nenhum` = 99 exclusivo e fixo; `Não sei` = 98; `Outro` fixo
- [ ] Listas de marcas/atributos com `(RODIZIAR)`
- [ ] Cliente não revelado na introdução
- [ ] `NOVA TELA:` antes de cada tela (online/CAPI)
- [ ] Encerramento + rodapé okno presentes
- [ ] Máx. 30 perguntas por seção sem aprovação
