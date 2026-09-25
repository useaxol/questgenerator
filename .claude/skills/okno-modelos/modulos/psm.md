# Módulo — PSM (Price Sensitivity Meter / Van Westendorp)

Referência real okno: teste Inco, P.64A–P.64D (escada de preços por produto, lógica de consistência) + P.65
intenção de compra com preço.

## Insumos (ficha)
- Unidade de venda exata (ex.: "pacote com 16 unidades", "garrafa de 1 L").
- Preço de referência atual e preço-alvo testado.
- **Escada de preços**: 20–35 degraus, de ~60% a ~180% do preço de referência, passo constante (ex.: R$ 1,96),
  uma coluna por produto/célula quando os preços de referência diferem. Se `Não tenho essa informação`, a IA
  monta a escada com base no preço de mercado da categoria e marca `[PROPOSTO PELA IA — VALIDAR]`.

## Posição
Depois da avaliação do produto/conceito e **antes** de qualquer pergunta com preço mostrado (para não ancorar).

## Perguntas (ordem okno: barato → barato demais → caro → caro demais)
Texto de abertura (NOVA TELA): "Se este produto estivesse à venda em ____ (UNIDADE) nos locais onde você costuma
comprar ____:"

- **P.xA** "A partir de qual preço este produto começa a parecer **barato**? (RU)"
- **P.xB** "A partir de qual preço este produto fica **barato demais**, a ponto de você duvidar da qualidade e decidir
  não comprar? (RU)" `PROGRAMAÇÃO: MOSTRAR APENAS PREÇOS IGUAIS OU MENORES QUE P.xA | SE P.xA FOR O MENOR PREÇO,
  REPETIR A RESPOSTA EM P.xB E NÃO APLICAR A PERGUNTA`
- **P.xC** "A partir de qual preço este produto começa a parecer **caro**? (RU)" `PROGRAMAÇÃO: MOSTRAR APENAS PREÇOS
  MAIORES QUE P.xA | SE O MAIOR PREÇO FOI SELECIONADO EM P.xA, NÃO APLICAR P.xC E P.xD`
- **P.xD** "A partir de qual preço este produto fica **caro demais**, a ponto de você não considerar comprá-lo? (RU)"
  `PROGRAMAÇÃO: MOSTRAR APENAS PREÇOS MAIORES QUE P.xC | SE P.xC JÁ FOR O MAIOR PREÇO, REPETIR A RESPOSTA EM P.xD E NÃO APLICAR A PERGUNTA`

Tabela única (uma coluna de preço por produto + colunas de código P.xA–P.xD):

| Produto 1 | Produto 2 | P.xA | P.xB | P.xC | P.xD |
|---|---|---|---|---|---|
| R$ 35,97 | R$ 30,20 | 1 | 1 | 1 | 1 |
| … | … | … | … | … | … |

## Complemento recomendado
- **Intenção de compra com preço** (escala 2) no preço-alvo: "Se este produto estivesse à venda… pelo preço de
  R$ ___ (PROGRAMAÇÃO: INSERIR PREÇO DA TABELA CONFORME O PRODUTO TESTADO) para ____ (UNIDADE), qual seria a sua intenção de compra?"
- (Opcional, extensão NMS) "E pelo preço de R$ ___ (preço barato de P.xA), qual seria…" / "…pelo preço de P.xC".

## Leitura (para o analista — não vai ao questionário)
Curvas acumuladas: barato demais e barato (decrescentes), caro e caro demais (crescentes). PMC = barato demais ×
caro; PME = barato × caro demais; OPP = barato demais × caro demais; IPP = barato × caro.

## Checagens do revisor
- Ordem das 4 perguntas e as 4 restrições de programação presentes.
- Escada monotônica, passo constante, cobre o preço atual e o testado.
- Unidade de venda idêntica em todas as perguntas de preço do questionário.
