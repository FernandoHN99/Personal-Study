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
- Demais (ações/ETF): `Moeda Base == "USD"` → Finnhub; senão → Alpha Vantage (`TIME_SERIES_DAILY`). Depois, **todo ativo não-FIAT/não-CRIPTO** é convertido para BRL via cotação da `Moeda Base` em `Table_Cotacoes` (`USD`, `EUR`, etc.). Alpha Vantage free ≈ 5 req/min.

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

## Plano de migração para VBA (macOS)

**Status:** Em implementação

Objetivo: replicar o comportamento do `main.py` como macro VBA dentro da planilha, acionável por botão no Excel.

**Por quê?** 
- Elimina dependência de Python/shell no fluxo operacional.
- Usuário clica botão → macro roda → planilha atualizada.
- Preserva gráficos, slicers, fórmulas (tudo fica no Excel).

**Decisões tomadas:**
1. **Arquivo base:** `.xlsm` (macro-enabled). `01-Nando-Din.xlsm` é o entry point.
2. **VBA puro, ZERO Python** no fluxo operacional. Um arquivo só, botão dispara tudo.
3. **HTTP nativo:** no macOS usa `MacScript()` com `do shell script "curl ..."`; no Windows usa `WinHttp.WinHttpRequest.5.1` (fallback `MSXML2.ServerXMLHTTP.6.0`). Tudo selecionado por `#If Mac Then`.
4. **JSON:** parser leve próprio (`modJson`), sem dependência externa (VBA-JSON não é necessário para as respostas simples destas APIs).
5. **Tabelas nativas:** `ListObject`, `ListRows.Add`, `DataBodyRange`. Colunas de fórmula da tabela se auto-preenchem ao adicionar linha (não sobrescrever).
6. **Sem `Scripting.Dictionary`:** o Excel para Mac NÃO tem Microsoft Scripting Runtime. Usamos a classe própria `KeyValueStore.cls` (`Item` default, `Exists`, `Count`) — funciona em Mac e Windows.
7. **Estrutura modular:**
   - `modConfig`: constantes, chaves API, nomes de tabelas/colunas, `GetFirstDayOfMonth`.
   - `KeyValueStore.cls`: substituto nativo do dicionário (classe).
   - `modHttp`: `HttpGet(url)` (macOS via `MacScript`+curl; Windows via WinHTTP) + `TesteHttp` para validar isolado.
   - `modJson`: `JsonGetNumberByKey`, `JsonGetStringByKey`, `JsonHasKey`.
   - `modTables`: `GetListObject`, `GetLastDateOfData`, `GetLastRows`, `DuplicateLastRowsToNewDate`.
   - `modQuotes`: `UpdateQuotes` (AwesomeAPI, Finnhub, Alpha Vantage, CoinGecko + conversão p/ BRL).
   - `modInvestments`: `UpdateInvestments` (duplica última leva das 2 tabelas se virou mês).
   - `modMain`: macro principal `AtualizarInvestimentos()`. Recalcula com `Application.CalculateFull` (NÃO `Workbook.RecalcAll`, que não existe).

**Fluxo da macro (`AtualizarInvestimentos`, VBA puro):**
1. Desabilitar `ScreenUpdating`, `EnableEvents`, cálculo automático.
2. **Investimentos:** `Table_Investimentos_Main` e `Table_Investimentos_Porcent` — se virou mês, duplicar última leva com `Data = 1º dia mês atual` (só valores; colunas de fórmula auto-preenchem). Se não virou: nada.
3. **Cotações:** ler última leva de `Table_Cotacoes`; buscar valor por ativo conforme `Tipo`/`Moeda Base`; se virou mês → inserir nova leva, senão → atualizar `Valor` no lugar.
4. **Timestamp:** `Última Atualização` + data/hora em `Cotacoes!A1:A2`.
5. Recalcular (`Application.CalculateFull`) e salvar.

**Roteamento de cotações (idêntico ao `main.py`):**
- `Tipo == "FIAT"` → AwesomeAPI (`/USD-BRL`, campo `bid`); `BRL` = 1.0 implícito.
- `Tipo == "CRIPTO"` → CoinGecko (`vs_currencies=brl`, campo `brl`).
  - Para tickers como `BTC`/`SOL`, o VBA resolve o `id` real do CoinGecko antes da consulta (`bitcoin`, `solana`).
- Ações/ETF `Moeda Base == "USD"` → Finnhub (campo `c`).
- Ações/ETF outra moeda → Alpha Vantage (`4. close`).
- Depois da busca, **todos os ativos não-FIAT/não-CRIPTO** são multiplicados pela cotação da `Moeda Base` para gravar `Valor` em BRL. Ex.: ETF em USD via Finnhub grava `preço USD * USDBRL`.

**Etapas de implementação:**
- [x] **Etapa 1** – Módulos VBA com estrutura base e helpers.
- [x] **Etapa 2** – HTTP nativo via `MacScript`+`curl` / WinHTTP.
- [x] **Etapa 3** – Cotações (fetch + insert/update) em VBA puro.
- [x] **Etapa 4** – Investimentos (duplicar/inserir).
- [ ] **Etapa 5** – Importar `.bas` + `KeyValueStore.cls`, criar botão e testar no Excel.
- [ ] **Etapa 6** – Validar preservação de gráficos, slicers, fórmulas.
- [ ] **Etapa 7** – Documentar adaptação para Windows (mesmo código deve rodar; validar).

**Arquivos VBA (importar nesta ordem):**
`modConfig.bas` → `KeyValueStore.cls` → `modHttp.bas` → `modJson.bas` → `modTables.bas` → `modQuotes.bas` → `modInvestments.bas` → `modMain.bas`

**Setup no Excel (macOS):**
1. Abrir `01-Nando-Din.xlsm`; `Option+F11` (VBE).
2. `VBAProject` → botão direito → `Import File` para cada `.bas` e a classe `KeyValueStore.cls` na ordem acima.
3. Voltar ao Excel → Inserir botão (Developer/Formulários) → vincular a `AtualizarInvestimentos`.
4. Clicar no botão. Na 1ª requisição, o macOS pode pedir permissão de rede → Permitir.

## Avisos

- **API keys** em `modConfig.bas` (Alpha Vantage / CoinGecko / Finnhub). Não vaze nem commite chaves novas.
- **`.xlsm` é o entry point** e é **VBA puro** — não depende mais de Python no fluxo. O `main.py` fica só como referência de comportamento.
- **HTTP no macOS:** `MacScript` roda `curl` embutido; no Windows usa WinHTTP/ServerXMLHTTP. Não há dependência de Python no fluxo.
- **Colunas de fórmula das tabelas de investimento** (ex.: `Cotação Ativo`, `Total (R$)`) se auto-preenchem — o código NÃO as sobrescreve. Só grava valores nas colunas manuais + `Data`.
- Binário PyInstaller de ~29MB (`fill-excel-investments`) e `.xlsx` real (dados financeiros) estão **commitados** no git, sem `.gitignore`. Não regenere/commite esses artefatos por descuido.
