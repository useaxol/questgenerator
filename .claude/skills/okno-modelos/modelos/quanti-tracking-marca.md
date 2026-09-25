# Modelo — Tracking de marca

Referências reais: JOB 183.25.002 Tracking de Marcas Cachaça (presencial, 1.500 entrevistas, 15 praças) e
JOB 267.25.006 Monitoramento de Marca Varejo moda (online, 2.000 entrevistas/trimestre). Guia §7.3 e §8.

## Particularidades de tracking
- **Comparabilidade entre ondas é prioridade**: não mudar enunciado, escala, ordem nem códigos de perguntas com série
  histórica. Mudanças são registradas no próprio questionário:
  "INCLUÍDA EM JULHO/24 E EXCLUÍDA EM NOVEMBRO/24" · "OCULTAR POR TEMPO INDEFINIDO" ·
  "APLICAR P.30 EM JULHO/26 E DEZEMBRO/26 / OCULTAR EM MARÇO/26 E SETEMBRO/26" ·
  "PN: QUESTIONS Q85 TO Q87 HAVE BEEN MOVED. PLACE THEM AFTER Q77." Numeração antiga é preservada (por isso há P.15
  "não existe" e P.20 antes de P.19). Perguntas novas recebem o próximo número livre, não renumeram.
- Onda nova de tracking existente: **peça o questionário da onda anterior** na etapa 2 e trabalhe sobre ele. A ficha
  registra `Onda de tracking existente? Sim/Não` — se Não, a numeração é sequencial nova.
- NPS e grids por marca: use as **marcas reais com seus códigos** nas linhas. `MARCA 1…N` só é aceito quando há
  tabela de marcas avaliadas por praça + instrução de pipe (padrão Cachaça).
- Todo nível do funil que pode ficar vazio precisa de `Nenhuma` (99) **ou** de pulo explícito (ex.: "SE NENHUMA MARCA EM P.16, PULE PARA P.19"); RU com base vazia trava a programação.
- Online: `GLOBAL QUALITY CHECK` (SPEEDER CHECK após Pxx; STRAIGHT LINE; perguntas de atenção) e `QUOTA_GRID` com metas.

## Sequência
1. **Cabeçalho + introdução + cotas** (sexo, idade, classe, praça).
2. **Triagem**: Critério Brasil → sexo → idade → área de atuação (ordem do Guia §9.1; o tracking de cachaça usa idade → sexo por herança) (+ estado civil opcional) → praça (estado/cidade com
   região metropolitana; outra cidade → ENCERRE) → raça/cor (online).
3. **Consumo da categoria**: frequência da categoria ampla e do segmento (escala de frequência, ENCERRE abaixo do
   mínimo) → funil de tipos (último ano → 1x/mês → maior frequência → preferida → rejeita → aumentou → diminuiu) com
   filtro "DEVE CITAR ____ (CÓD X) EM P.8" → locais de compra (RM, com Outro especifique).
4. **Top of mind** (opcional, varejo): "Quando você pensa em ____, qual é a primeira marca que vem à sua cabeça? [OE]".
5. **Pirâmide de marcas** completa (ver `okno-linguagem/references/funil-de-marcas.md` §2) com tabela única,
   marcas regionais `(MOSTRAR APENAS EM <PRAÇA>)`, filtro "SE NÃO CONHECER NENHUMA DAS MARCAS AVALIADAS DA PRAÇA, ENCERRE",
   e pergunta de ruptura por marca.
6. **NPS e avaliação das marcas**: tabela de marcas avaliadas por praça (máx. 7 por entrevistado), só marcas
   conhecidas; NPS 0–10 por marca em rodízio; follow-ups da marca-cliente (0–8 melhorar / 9–10 razões, "DEVEMOS TER
   PELO MENOS 2 RAZÕES").
7. **Imagem de marca**: associação marcas × atributos (mesmas marcas do NPS, atributos em rodízio, Nenhuma / Não sabe).
   Opcional: atratividade 0–10, preço × valor ("Os produtos são mais caros que outras lojas, mas vale a pena pagar"…).
8. **Recall de comunicação**: espontâneo → estimulado (tabela única; 98 Não lembro / 99 Nenhuma) → meio → conteúdo;
   ativações específicas (placas de estádio, patrocínio) com lista de marcas do meio.
9. **Aprofundamentos da marca-cliente** (varejo): barreiras por gap do funil (conhece e não visita / visita e não compra;
   físico e online separados) com "principal motivo" e diagnóstico "O que você quis dizer com isso?"; assinatura/slogan
   (lembra? → qual? → o quanto combina 0–10).
10. **Aceite de compartilhamento de contato** com o cliente (revela o cliente só aqui, se pedido).
11. **Encerramento** + VOLTAS DE CAMPO | COMENTÁRIOS DE CAMPO + rodapé.

## Objetivos típicos → blocos / KPIs
| Objetivo | KPI |
|---|---|
| Saúde de marca / funil | % conhecimento esp./est., experimentação, uso 6m, uso habitual, BUMO, preferida; conversões entre níveis |
| Lealdade / risco | Reduziu, parou, rejeita; ruptura (compra outra vs. vai a outro lugar) |
| Recomendação | NPS por marca + drivers (abertas 0–8 / 9–10) |
| Posicionamento | Imagem (associação) vs. concorrentes; atributos-alvo do posicionamento |
| Efetividade de comunicação | Recall esp./est., meio, conteúdo, atribuição correta |
| Canais | Locais de compra; online × físico (CANAL = online/offline/omni) |
