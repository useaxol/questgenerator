# Referências

## 1. Referências okno (fonte dos padrões das skills)

Os arquivos originais ficam no Google Drive (pasta **Okno**) e **não** são copiados para o git (contêm dados e
classificações de clientes). As skills `okno-linguagem` e `okno-modelos` já trazem os padrões extraídos deles.
Com o conector do Google Drive ativo, o gerador pode abri-los pelo ID para espelhar a estrutura.

| Arquivo | Drive fileId | Tipo de estudo | Padrões extraídos |
|---|---|---|---|
| okno_questionario_style_guide_v1.docx | `11P83JkGiFeUkHag0P9U095xNg9YrdIGO` | Guia de estilo v1.0 (2026) | Estrutura, códigos, escalas, blocos fixos, pirâmide de marcas, mapa de referências |
| Brand Tracking - Bebidas Alcoólicas.docx | `1k2K2eL2RBr6hPhER86fbtmJ4MARpwmbo` | Tracking presencial (JOB 183.25.002, cachaça) | Critério Brasil 2026, funil de categoria em tabela única, pirâmide completa, NPS + follow-ups, imagem, recall |
| Brand Tracking - Varejo.docx | `12EY-qDCkypF3eiBsKVSZEJPU3vtspjEP` | Tracking online (JOB 267.25.006, moda) | QUOTA_GRID, PUNCH HIDE, PIPE CODES, AUTO PUNCH, carrossel, funil de lojas, barreiras por gap, controle de ondas |
| Teste de Produto Recrutamento - Higiene Pessoal (Inco).docx | `1LVsei94FcjnCgAWrgctYHhiItzUmYKVs` | Recrutamento HUT (JOB 88.24.010, EN) | Painéis, funil de uso, repertório de marcas com filtro, pantry check, baseline do habitual, convite, LGPD |
| Teste de Produto Quest Principal - Higiene Pessoal (Inco).docx | `1w19hu3RPbIeWe1lldceLNVKKNzSuEOln` | Avaliação HUT monádica sequencial (EN) | Checagem de código, avaliação global, grids por dimensão, JAR, PSM 64A–D, comparação, conceito, embalagem, nomes, selos |

## 2. Benchmarks de mercado (`benchmarks/`)

Resumos estruturais de questionários Kantar Insights (Conjoint, Pack, Conceito, CPT, Segmentação Matrix), usados
**só como referência de estrutura** para tipos sem modelo okno. Quando divergirem do padrão okno (ex.: escalas de 4,
7 ou 9 pontos), vale o padrão okno.

## 3. Inconsistências encontradas no Guia de Estilo v1.0 (para a okno corrigir)

1. **Critério Brasil**: o texto manda usar "Novo Critério Brasil 2026", mas a tabela de pontos (§4) é a do critério
   2015–2024 (classes A 45–100 … DE 0–16). O tracking de fev/2026 já usa a versão 2026 (A 73–100 … DE- 0–10, 7 classes).
   As skills trazem as duas versões e pedem confirmação na descoberta.
2. **Serviços públicos (§4)**: a linha "Ensino superior completo — 2 pts" deveria ser **"Rua pavimentada — 2 pts"**.
3. **Pirâmide (§8)**: P.20 (já experimentou) aparece antes de P.19 (consumiu 6 meses) por herança do tracking; em
   questionários novos a numeração deve ser sequencial.
4. **Pirâmide reduzida (§8.1)**: "Já experimentou" tem base "P18", que não existe na versão reduzida; a base correta é
   o conhecimento estimulado (P.17).
5. **Ordem da triagem**: §9.1 diz Critério Brasil → Sexo → Idade → Área; os questionários reais variam
   (Cachaça: Critério → Idade → Sexo → Área; Inco: Critério no fim). As skills seguem o Guia e aceitam variação só por
   pedido do briefing.
