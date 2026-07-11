# AGENTS.md — project-fill-excel-investments

Script Python (PT-BR) que lê a planilha de investimentos `.xlsx`, busca cotações em APIs e reescreve as tabelas no próprio arquivo. Escopo: **apenas esta pasta** (o repo git é a pasta pai `Python/`, que agrega vários projetos de estudo).

## Rodar

```bash
pip install -r requirements.txt   # openpyxl, pandas, msoffcrypto-tool, requests
python3 main.py                   # pede senha no terminal; ENTER vazio = sem senha
python3 search.py                 # busca ticker/símbolo por nome (Alpha Vantage)
```

- `main.py` é um script solto (sem package/funções `main()`): o bloco `try` no fim (linhas 361+) executa tudo no import.
- Descobre sozinho o **primeiro** arquivo `.xlsx/.xlsm/...` da pasta (`get_excel_file`). Hoje: `01-Nando-Din.xlsx`.
- A planilha **não é mais protegida por senha** — deixe a senha vazia. O ramo msoffcrypto (decrypt/encrypt) só importa se você digitar uma senha.

## Planilha é o contrato (VERIFICADO)

Sheets reais: `Investimentos_Main`, `Investimentos_Porcent`, `Cotacoes`, `Graficos`, `Tables_Atual_Ideal`, `Gastos_Mensais`, `Previdencia`.

Tabelas que o script manipula (nomes atuais, já renomeados na planilha):

| Fluxo | Sheet | Tabela | Colunas |
|-------|-------|--------|---------|
| Cotação | `Cotacoes` | `Table_Cotacoes` | `Data, Ticker, Valor, Moeda Base, Tipo` |
| Investimento (quantidades) | `Investimentos_Main` | `Table_Investimentos_Main` | `Data, Nome, Ticker, Instituição, Estratégia, Quantidade, Cotação Ativo, Moeda Base, Cotação Dolar, Total (R$)` |
| Investimento (percentual) | `Investimentos_Porcent` | `Table_Investimentos_Porcent` | `Data, Nome, Classe, Subclasse, Duração, Estratégia, Moeda Base, Porcentagem, Total (R$), Total ($)` |

- O código lê sheet/tabela por nome fixo (bloco Env Vars) e referencia colunas por nome (não por posição).
- As duas tabelas de investimento só precisam da coluna `Data` no fluxo — os valores (cotação/total) vêm de lookups dentro da própria planilha, então o script apenas **duplica** a última leva por virada de mês.

## Plano de migração (nomes novos das tabelas)

Objetivo: manter o comportamento de hoje apontando para as tabelas renomeadas, e passar a manipular **as duas** tabelas de investimento (`Table_Investimentos_Main` e `Table_Investimentos_Porcent`) com o mesmo comportamento de virada de mês.

Decisões: (1) investimento só **duplica** a última leva trocando `Data` (lookups na planilha já puxam cotação); (2) colunas referenciadas por **nome fixo**; (3) mês não virou → investimento não faz nada, só cotação atualiza no lugar.

- [x] **Etapa 1** — Env Vars: `TABLE_QUOTE_NAME="Table_Cotacoes"`; substituir o par único de investimento por `SHEET/TABLE_INVEST_MAIN` e `SHEET/TABLE_INVEST_PORCENT`.
- [x] **Etapa 2** — `start_flow_quote`: mapear colunas por nome (`"Data"`, `"Ticker"`, `"Valor"`, `"Moeda Base"`, `"Tipo"`) em vez de `header[0..4]`.
- [x] **Etapa 3** — Generalizar `start_flow_investiment(wb, date_today, sheet, table)`: lê → `max(Data)` → se mês virou, duplica e insere; senão nada. Remove as globais erradas de 11 colunas.
- [x] **Etapa 4** — No `main`, chamar o fluxo para `Table_Investimentos_Main` e `Table_Investimentos_Porcent`.
- [x] **Etapa 5** — Migração para xlwings: trocar `openpyxl` por `xlwings` para preservar gráficos/slicers. Implementado em `main.py` com funções `get_table_ranges()`, `read_table_xlwings()`, `write_table_xlwings()`, `insert_table_xlwings()`.
- [x] **Etapa 6** — Rodar teste com data real: cotações atualizadas, gráficos/slicers **preservados**. **Resultado: Sucesso. Slicers=True, Charts=True.**
- [x] **Etapa 7** — Testar com agosto/2026 (simulação de virada de mês e inserção de investimentos). **Resultado: Sucesso. Main +20 linhas, Porcent +26 linhas, Cotações +12 linhas. Slicers=True, Charts=True.**
- [x] **Etapa 8** — Reconciliar este AGENTS.md com o estado final. **Completo: xlwings + macOS + gráficos/slicers preservados.**

## Padrões/armadilhas do código

- `start_flow_quote` usa globais (`DATE_COL`, `TICKER_COL`, `VALUE_COL`, `CURRENCY_BASE_COL`, `TYPE_COL`) atribuídas com **nomes fixos** (não por posição); não existem antes da função rodar.
- `start_flow_investiment` recebe sheet/table como parâmetros e usa apenas a coluna `"Data"` por nome; não precisa de globais para mapear as outras colunas.
- `ler_tabela_para_dicionarios` injeta a coluna extra `REF_COL = "Ref Cells"` com as coordenadas `(row, col)` de cada célula; os fluxos de escrita dependem dela ser o **último** item de cada linha (`row[-1]`). Ao mexer nos DataFrames, preserve essa coluna no fim.
- `openpyxl` desta versão: `ws._tables` é dict `{nome: <Table>}`, e `table.ref` dá o range (ex.: `B4:K327`). Use `range_boundaries`/`get_column_letter` como já feito.
- Insert vs. Update por data: compara `df["Data"].max()` com o 1º dia do mês atual (`get_current_date_start_of_month`). Insere linhas novas só quando muda o mês; senão não faz nada (cotação atualiza no lugar, investimento não).
- Imports pesados (openpyxl/pandas/requests/msoffcrypto) ficam **no fim, dentro do `try`** — não no topo. Rodar funções isoladas fora do fluxo principal falha por import ausente.

## Roteamento de cotações (por coluna `Tipo`/`Moeda Base` da aba `Cotacoes`)

- `Tipo == "FIAT"` → AwesomeAPI (`BRL` é ignorado, fica 1.0 implícito).
- `Tipo == "CRIPTO"` → CoinGecko.
- Demais (ações/ETF): `Moeda Base == "USD"` → Finnhub; senão → Alpha Vantage (`TIME_SERIES_DAILY`), depois convertido p/ BRL via cotação da moeda. Alpha Vantage free ≈ 5 req/min.

## Migração para xlwings (Preserva gráficos e slicers)

A partir de agora, o script usa **xlwings** para abrir/manipular/salvar a planilha, em vez de `openpyxl`. 

**Por quê?** xlwings controla o **Excel real** (via AppleScript no macOS, via COM no Windows), então o arquivo é manipulado e salvo pelo próprio Excel. Isso preserva:
- ✅ Gráficos (charts)
- ✅ Slicers (segmentação de dados)
- ✅ Pivot tables
- ✅ Validações customizadas
- ✅ Proteção de planilha
- ✅ Macros/VBA (no Windows)

**Requisitos:**
- Excel instalado e acessível no macOS (via AppleScript).
- Na primeira execução no macOS, o sistema pode pedir permissão para Python controlar o Excel → **Permitir**.

**Limitação:**
- xlwings **não suporta planilhas protegidas por senha** (a implementação atual rejeita com erro se tentar passar senha). A planilha precisa estar sem senha.

## Avisos

- **API keys hardcoded** em `main.py` (Alpha Vantage / CoinGecko / Finnhub) e `search.py`. Não vaze nem commite chaves novas.
- Binário PyInstaller de ~29MB (`fill-excel-investments`) e o `.xlsx` real (dados financeiros) estão **commitados** no git, sem `.gitignore`. Não regenere/commite esses artefatos por descuido.
- Build do binário: `pyinstaller` (sem `.spec` no repo).
