# Checklist de descoberta — ficha do projeto

Copie o modelo abaixo para `projetos/<slug>/ficha-projeto.md` e preencha. Coluna **Fonte**: `arquivo › trecho`,
`USUÁRIO` (respondido na etapa 2) ou `[PROPOSTO PELA IA — VALIDAR]`.

**Essencial** = sem ele não se constrói; pergunte se não encontrar. **Opcional** = use padrão okno se faltar.

```markdown
# Ficha do projeto — <nome>

## 1. Identificação
| Campo | Valor | Fonte | Nível |
|---|---|---|---|
| Cliente (empresa / marca) | | | Essencial |
| Categoria / produto | | | Essencial |
| JOB okno (nnn.aa.nnn) | | | Opcional (JOB [A DEFINIR]) |
| Nome do estudo | | | Opcional |
| Idioma do questionário (PT / EN / bilíngue) | | | Opcional (PT) |
| Classificação do documento (ex.: CLIENT INTERNAL) | | | Opcional |

## 2. Objetivo e áreas de abordagem
| Campo | Valor | Fonte | Nível |
|---|---|---|---|
| Objetivo principal (decisão de negócio) | | | Essencial |
| Objetivos específicos / áreas de abordagem (lista numerada O1, O2…) | | | Essencial |
| Hipóteses do cliente | | | Opcional |
| KPIs / action standards (ex.: top 2 box ≥ X%, paridade vs. habitual) | | | Opcional |

## 3. Metodologia
| Campo | Valor | Fonte | Nível |
|---|---|---|---|
| Abordagem (quali / quanti / híbrido) | | | Essencial |
| Tipo de questionário (ver etapa 3) | | | Essencial |
| Técnica de coleta (online, CAPI, CATI, face a face, CLT, HUT, GD, EP, etnografia) | | | Essencial |
| Desenho (monádico, monádico sequencial, pareado, blind/branded, nº de células) | | | Essencial p/ testes |
| Duração da entrevista / sessão | | | Opcional (quanti 15–20 min; GD 120 min; EP 60 min) |
| Nº de entrevistas / grupos / células | | | Essencial |
| Ondas (tracking) e comparabilidade com ondas anteriores | | | Essencial p/ tracking |

## 4. Público e amostra
| Campo | Valor | Fonte | Nível |
|---|---|---|---|
| Público-alvo (definição) | | | Essencial |
| Sexo | | | Essencial |
| Faixas etárias | | | Essencial |
| Classes sociais aceitas + versão do Critério Brasil | | | Essencial (versão: opcional → 2026) |
| Praças / regiões | | | Essencial |
| Critério de uso da categoria (frequência mínima, tempo de uso, compra própria) | | | Essencial |
| Marcas usuárias exigidas / rejeições proibidas | | | Conforme estudo |
| Cotas (cruzamentos e metas) | | | Opcional |
| Filtros adicionais (saúde, alergias, gravidez, deficiência, participação em pesquisa) | | | Opcional |

## 5. Estímulos e listas
| Campo | Valor | Fonte | Nível |
|---|---|---|---|
| Produtos / códigos de amostra / painéis de rotação | | | Essencial p/ teste de produto |
| Conceitos, embalagens, peças de comunicação (qtde, formato, tempo de exposição) | | | Essencial p/ testes |
| Lista de marcas (ordem, códigos históricos, regionais) | | | Essencial p/ funil de marcas |
| Lista de atributos / dimensões / imagem | | | Essencial p/ grids |
| Preços (atual, testado, escada para PSM) | | | Essencial p/ PSM/intenção com preço |
| Concorrentes de referência | | | Opcional |

## 6. Módulos
| Módulo | Aplica? | Insumos | Fonte |
|---|---|---|---|
| Conjoint (CBC) | | atributos × níveis, nº tarefas, conceitos/tela, opção nenhum, proibições | |
| MaxDiff | | lista de itens (8–30), itens/tela, nº de telas, versões | |
| PSM (Van Westendorp) | | escada de preços, unidade/embalagem, preço para intenção | |

## 7. Quali (se aplicável)
| Campo | Valor | Fonte |
|---|---|---|
| Nº de grupos / EPs e composição de cada um | | |
| Duração da sessão e formato (presencial / online) | | |
| Tarefas pré-campo desejadas (fotos, diário, colagem, vídeo) | | |
| Estímulos a expor no campo e ordem | | |
| Técnicas projetivas desejadas | | |
| Incentivo, data e local | | |

## 8. Mapa objetivo → blocos (preencher na etapa 3)
| Objetivo | Bloco(s) previstos | Pergunta-chave / KPI |
|---|---|---|

## 9. Pendências [PROPOSTO PELA IA — VALIDAR]
- …
```

## Perguntas-modelo para a etapa 2 (AskUserQuestion)

Sempre com `Não tenho essa informação` como última opção. Exemplos:

- **Público** — "Qual a faixa etária do público-alvo?" → "18 a 60 anos" · "25 a 65 anos" · "Não tenho essa informação"
- **Classe** — "Quais classes sociais participam?" → "A, B e C" · "B e C" · "Não tenho essa informação"
- **Critério Brasil** — "Qual versão do Critério Brasil usar?" → "Novo Critério Brasil 2026" · "Critério Brasil 2024" · "Não tenho essa informação"
- **Técnica** — "Como será a coleta?" → "Online (painel)" · "Presencial CAPI / CLT" · "HUT (em casa)" · "Não tenho essa informação"
- **Módulos** (multiSelect) — "Algum módulo adicional?" → "PSM" · "MaxDiff" · "Conjoint" · "Não tenho essa informação"
- **Desenho** — "Como os produtos serão avaliados?" → "Monádico" · "Monádico sequencial (rodízio)" · "Pareado" · "Não tenho essa informação"

Quando o usuário escolher `Não tenho essa informação`, proponha o valor, justifique em uma linha e siga.
