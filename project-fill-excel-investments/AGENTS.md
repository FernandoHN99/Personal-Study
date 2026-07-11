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
- [ ] **Etapa 2** — `start_flow_quote`: mapear colunas por nome (`"Data"`, `"Ticker"`, `"Valor"`, `"Moeda Base"`, `"Tipo"`) em vez de `header[0..4]`.
- [ ] **Etapa 3** — Generalizar `start_flow_investiment(wb, date_today, sheet, table)`: lê → `max(Data)` → se mês virou, duplica e insere; senão nada. Remove as globais erradas de 11 colunas.
- [ ] **Etapa 4** — No `main`, chamar o fluxo para `Table_Investimentos_Main` e `Table_Investimentos_Porcent`.
- [ ] **Etapa 5** — Rodar e validar (Excel pode precisar ser fechado p/ salvar). Mês atual já existe → esperado: cotações atualizam, investimentos inalterados.
- [ ] **Etapa 6** — Reconciliar este AGENTS.md com o estado final.

## Padrões/armadilhas do código

- Nomes de coluna viram **globais** (`DATE_COL`, `TICKER_COL`, `TYPE_COL`...) atribuídas dentro de `start_flow_quote`/`start_flow_investiment`. Não existem antes do fluxo rodar, e os dois fluxos sobrescrevem `DATE_COL`/`TYPE_COL`.
- `ler_tabela_para_dicionarios` injeta a coluna extra `REF_COL = "Ref Cells"` com as coordenadas `(row, col)` de cada célula; os fluxos de escrita dependem dela ser o **último** item de cada linha (`row[-1]`). Ao mexer nos DataFrames, preserve essa coluna no fim.
- `openpyxl` desta versão: `ws._tables` é dict `{nome: <Table>}`, e `table.ref` dá o range (ex.: `B4:K327`). Use `range_boundaries`/`get_column_letter` como já feito.
- Insert vs. Update por data: compara `df[DATE_COL].max()` com o 1º dia do mês atual (`get_current_date_start_of_month`). Insere linhas novas só quando muda o mês; senão atualiza a última leva no lugar.
- Imports pesados (openpyxl/pandas/requests/msoffcrypto) ficam **no fim, dentro do `try`** — não no topo. Rodar funções isoladas fora do fluxo principal falha por import ausente.

## Roteamento de cotações (por coluna `Tipo`/`Moeda Base` da aba `Cotacoes`)

- `Tipo == "FIAT"` → AwesomeAPI (`BRL` é ignorado, fica 1.0 implícito).
- `Tipo == "CRIPTO"` → CoinGecko.
- Demais (ações/ETF): `Moeda Base == "USD"` → Finnhub; senão → Alpha Vantage (`TIME_SERIES_DAILY`), depois convertido p/ BRL via cotação da moeda. Alpha Vantage free ≈ 5 req/min.

## Avisos

- **API keys hardcoded** em `main.py` (Alpha Vantage / CoinGecko / Finnhub) e `search.py`. Não vaze nem commite chaves novas.
- Binário PyInstaller de ~29MB (`fill-excel-investments`) e o `.xlsx` real (dados financeiros) estão **commitados** no git, sem `.gitignore`. Não regenere/commite esses artefatos por descuido.
- Build do binário: `pyinstaller` (sem `.spec` no repo).
