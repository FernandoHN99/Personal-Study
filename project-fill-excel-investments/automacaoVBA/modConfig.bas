Attribute VB_Name = "modConfig"
'==============================================================================
' modConfig - Configurações Centralizadas
'==============================================================================
' Constantes globais: nomes de sheets, tabelas, colunas, API keys

Option Explicit

' *** SHEETS ***
Public Const SHEET_COTACOES As String = "Cotacoes"
Public Const SHEET_INVESTIMENTOS_MAIN As String = "Investimentos_Main"
Public Const SHEET_INVESTIMENTOS_PORCENT As String = "Investimentos_Porcent"

' *** TABELAS ***
Public Const TABLE_COTACOES As String = "Table_Cotacoes"
Public Const TABLE_INVESTIMENTOS_MAIN As String = "Table_Investimentos_Main"
Public Const TABLE_INVESTIMENTOS_PORCENT As String = "Table_Investimentos_Porcent"

' *** COLUNAS COTACOES ***
Public Const COL_COTACOES_DATA As String = "Data"
Public Const COL_COTACOES_TICKER As String = "Ticker"
Public Const COL_COTACOES_VALOR As String = "Valor"
Public Const COL_COTACOES_MOEDA_BASE As String = "Moeda Base"
Public Const COL_COTACOES_TIPO As String = "Tipo"

' *** COLUNAS INVESTIMENTOS ***
Public Const COL_INVEST_DATA As String = "Data"

' *** TIPOS DE ATIVOS ***
Public Const TYPE_FIAT As String = "FIAT"
Public Const TYPE_CRIPTO As String = "CRIPTO"

' *** API KEYS (PRIVADO - NÃO COMMITE) ***
Public Const API_KEY_ALPHA As String = "J9OM0X9200KP47G2"
Public Const API_KEY_GECKO As String = "CG-ayNYBkPDUfbHRwk4MbWVrYiE"
Public Const API_KEY_FINNHUB As String = "d3o1m79r01qmj82ve8jgd3o1m79r01qmj82ve8k0"

' *** URLs BASE ***
Public Const API_URL_ALPHA_VANTAGE As String = "https://www.alphavantage.co/query"
Public Const API_URL_FINNHUB As String = "https://finnhub.io/api/v1/quote"
Public Const API_URL_AWESOME_API As String = "https://economia.awesomeapi.com.br/json/last/"
Public Const API_URL_COINGECKO As String = "https://api.coingecko.com/api/v3/simple/price"

' *** CONFIGURAÇÕES ***
Public Const TIMEOUT_HTTP As Long = 30000 ' milissegundos
Public Const DELAY_ALPHA_VANTAGE As Double = 0.15 ' segundos entre requisições (5 req/min)
Public Const DELAY_FINNHUB As Double = 0.05
Public Const DELAY_AWESOME As Double = 0.1
Public Const DELAY_COINGECKO As Double = 0.1

' *** HELPER: primeiro dia do mes (padrao = hoje) ***
Public Function GetFirstDayOfMonth(Optional refDate As Date = 0) As Date
    If refDate = 0 Then refDate = Date
    GetFirstDayOfMonth = DateSerial(Year(refDate), Month(refDate), 1)
End Function

' Obs.: GetLastDateOfData fica em modTables (evita nome duplicado).
