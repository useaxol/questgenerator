# questgenerator — questionários okno em loop

Sistema para Claude Code que gera questionários da **okno Núcleo de Estudos** a partir dos arquivos do projeto,
na linguagem okno, com revisão automática por um **analista sênior** até a aprovação.

## Como usar

1. Crie a pasta do projeto e coloque lá tudo o que existir (briefing, proposta, e-mails, questionário anterior,
   lista de marcas, estímulos):
   ```
   projetos/<nome-do-projeto>/entrada/
   ```
2. Abra o Claude Code na raiz do repositório e peça, por exemplo:
   > Crie o questionário do projeto `<nome-do-projeto>`

   ou chame direto a skill: `/okno-questionario <nome-do-projeto>`.
3. Responda às perguntas que o sistema fizer. Todas trazem a opção **"Não tenho essa informação"**. Nesse caso a IA
   propõe o dado com base no que tiver disponível e o marca como `[PROPOSTO PELA IA — VALIDAR]`.
4. Receba em `projetos/<nome-do-projeto>/`:
   - `ficha-projeto.md`: cliente, objetivo, metodologia, público, módulos, com a fonte de cada informação
   - `<tipo>-v<N>.md`: questionário no formato intermediário, uma versão por rodada do loop
   - `revisao-v<N>.md`: parecer do analista sênior em cada rodada
   - `<tipo>-v<N>.docx`: questionário final no padrão visual okno

## O loop

```
1 DESCOBERTA ─► 2 LACUNAS ─► 3 TIPO + MÓDULOS ─► 4 CONSTRUÇÃO
   (lê arquivos)  (pergunta c/        (quali/quanti,      (skill de linguagem okno
                  "Não tenho essa     Conjoint/MaxDiff/    + modelo da metodologia
                   informação")       PSM)                 + checador automático)
                                                                 │
8 PRÓXIMO DOCUMENTO ◄─ 7 EXPORTA .docx ◄─ 6 CORREÇÃO ◄─► 5 ANALISTA SÊNIOR
   (ex.: recrutamento →                  (até APROVADO      (1) pulos  (2) linguagem okno
    principal)                            ou 3 rodadas)     (3) cobertura do briefing
```

## Tipos suportados

| Qualitativo | Quantitativo | Módulos (quanti) |
|---|---|---|
| Questionário de recrutamento | Projeto ad hoc | Conjoint (CBC) |
| Pré-tarefa (GD / EP) | Teste de produto (recrutamento + principal) | MaxDiff |
| Roteiro de discussão | Teste de embalagem | PSM (Van Westendorp) |
| | Teste de comunicação | |
| | Tracking de marca | |
| | Diário de uso | |

## De onde vêm os padrões

A skill `okno-linguagem` foi construída a partir do **Guia de Estilo okno v1.0** e de 4 questionários reais da okno
(Tracking Cachaça, Monitoramento Varejo, Teste de Produto Inco com recrutamento e principal). Os padrões extraídos
incluem o funil de marcas em tabela única, as regras de pulo, pipe e transferência, os blocos fixos e as escalas.
Os modelos quali e os módulos também usam benchmarks de mercado (`referencias/benchmarks/`). Veja
`referencias/README.md` para o índice dos arquivos e as inconsistências encontradas no guia.

Para acrescentar novos questionários de referência, ponha-os no Drive (pasta Okno) ou em `referencias/` e peça ao
Claude: *"atualize as skills okno com os padrões deste questionário"*.

## Scripts

```bash
pip install -r requirements.txt
python3 scripts/extrair_texto.py projetos/<slug>/entrada/          # lê docx/pptx/xlsx/pdf
python3 scripts/checar_questionario.py projetos/<slug>/<arq>.md     # pulos, referências, escalas, placeholders
python3 scripts/gerar_docx.py projetos/<slug>/<arq>.md              # exporta .docx okno
```

Exemplo pronto para testar: `projetos/_exemplo-tracking-cachaca/`.
