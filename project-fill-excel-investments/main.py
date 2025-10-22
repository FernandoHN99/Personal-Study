# -------- Importações ---------
# from openpyxl import load_workbook
# from openpyxl.utils import get_column_letter, range_boundaries
# import io
import os
# import msoffcrypto
# import pandas as pd
# from datetime import datetime, date
# import requests
# import time
# import warnings
# from copy import copy
import getpass
# from msoffcrypto.format.ooxml import OOXMLFile
import sys
# -------- Funções Utils ---------

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def get_excel_file():
    base_dir = get_base_path()
    excel_exts = ('.xlsx', '.xlsm', '.xltx', '.xltm')
    for file_name in os.listdir(base_dir):
        if file_name.lower().endswith(excel_exts):
            return os.path.join(base_dir, file_name)
    return None

def clean_terminal():
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')

def open_workbook_with_password(file_path, password):
    decrypted_workbook = io.BytesIO()
    with open(file_path, "rb") as file:
        office_file = msoffcrypto.OfficeFile(file)
        office_file.load_key(password=password)
        office_file.decrypt(decrypted_workbook)
    
    decrypted_workbook.seek(0)
    return decrypted_workbook


def ler_tabela_para_dicionarios(ws, table):
    header = []
    table_data = []
    is_header = True

    for row in ws[table.ref]:
        row_values = [cell.value for cell in row]
        row_cells = [(cell.row, cell.column) for cell in row]

        if is_header:
            header = row_values
            is_header = False
        else:
            row_dict = dict(zip(header, row_values))
            row_dict[REF_COL] = row_cells
            table_data.append(row_dict)
            
    return header, table_data

def copy_format_from_above(cell, cell_acima):
    if not cell_acima or not cell_acima.has_style:
        return
    # Estilos visuais básicos
    cell.font = copy(cell_acima.font)
    cell.border = copy(cell_acima.border)
    cell.fill = copy(cell_acima.fill)
    # Formato numérico e alinhamento
    cell.number_format = copy(cell_acima.number_format)
    cell.alignment = copy(cell_acima.alignment)
    # Proteção (caso a planilha use)
    cell.protection = copy(cell_acima.protection)

def safe_upsert_data(cell, value, cell_above):
    BASIC_TYPES = (int, float, str, bool, type(None), date)
    if isinstance(value, BASIC_TYPES):
        cell.value = value
    else:
        cell.value = value.text
    copy_format_from_above(cell, cell_above)

def insert_data_from_df(ws_base, table_base, df_base):
    min_col, min_row, max_col, max_row = range_boundaries(table_base.ref)
    cell_row = max_row + 1

    for row in df_base.itertuples(index=False):
        length_row = len(row)
        for col_idx, value in enumerate(row):
            if col_idx >= (length_row - 1):
                continue

            cell_col = row[-1][col_idx][1]
            cell = ws_base.cell(row=cell_row, column=cell_col)
            cell_above = ws_base.cell(row=cell_row - 1, column=cell_col)
            safe_upsert_data(cell, value, cell_above)

        cell_row += 1

    table_base.ref = f"{get_column_letter(min_col)}{min_row}:{get_column_letter(max_col)}{cell_row - 1}"

def update_data_from_df(ws_base, table_base, df_base):
    min_col, min_row, max_col, max_row = range_boundaries(table_base.ref)
    cell_row = max_row + 1
    
    for row in df_base.itertuples(index=False):
        length_row = len(row)
        for col_idx, value in enumerate(row):
            if(col_idx >= (length_row -1)):
                continue
            cell_row = row[-1][col_idx][0]
            cell_col = row[-1][col_idx][1]
            
            cell = ws_base.cell(row=cell_row, column=cell_col)
            cell_above = ws_base.cell(row=cell_row - 1, column=cell_col)
            safe_upsert_data(cell, value, cell_above)

def upsert_table_excel_data(wb_base, ws_base, table_base, df_base, is_insert):
    if is_insert:
        insert_data_from_df(ws_base, table_base, df_base)
    else:
        update_data_from_df(ws_base, table_base, df_base)

def fetch_assets_global(df):
    list_new_values = []
    print("=== Atualizando cotações (Alpha Vantage) ===")

    for symbol in df[TICKER_COL]:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY_ALPHA}"
        res = requests.get(url)
        data = res.json()

        if "Time Series (Daily)" in data:
            last_date = list(data["Time Series (Daily)"].keys())[0]
            close = float(data["Time Series (Daily)"][last_date]["4. close"])
            list_new_values.append(close)
        else:
            list_new_values.append('Error')

        # Alpha Vantage free = ~5 requisições por minuto
        time.sleep(0.15)

    df_novo = df.copy()
    df_novo[VALUE_COL] = list_new_values
    return df_novo

def fetch_assets_us(df):
    list_new_values = []
    base_url = "https://finnhub.io/api/v1/quote"
    headers = {"X-Finnhub-Token": API_KEY_FINNHUB}

    print("=== Atualizando cotações (Finnhub) ===")

    for symbol in df[TICKER_COL]:
        try:
            url = f"{base_url}?symbol={symbol}"
            res = requests.get(url, headers=headers)
            data = res.json()

            if res.status_code == 200 and "c" in data:
                list_new_values.append(float(data["c"]))
            else:
                print(f"⚠️ Erro ao consultar {symbol}: {data}")
                list_new_values.append("Error")

        except Exception as e:
            print(f"⚠️ Erro ao consultar {symbol}: {e}")
            list_new_values.append("Error")

        time.sleep(0.05)

    df_novo = df.copy()
    df_novo[VALUE_COL] = list_new_values
    return df_novo


def fetch_currencies(df):
    print("=== Atualizando cotações (AwesomeAPI) ===")

    symbols_str = ",".join([f"{ticker}-BRL" for ticker in df[TICKER_COL]])
    url = f"https://economia.awesomeapi.com.br/json/last/{symbols_str}"

    list_new_values = []

    res = requests.get(url)
    data = res.json()

    for ticker in df[TICKER_COL]:
        key = f"{ticker}BRL"  # Ex: "USDBRL"
        if key in data:
            close = float(data[key]["bid"])
            list_new_values.append(close)
        else:
            list_new_values.append("Error")

        time.sleep(0.1)

    df_novo = df.copy()
    df_novo[VALUE_COL] = list_new_values

    return df_novo


def fetch_criptos(df):
    print("=== Atualizando cotações (CoinGecko) ===")

    ids_str = ",".join(df[TICKER_COL])
    url = f"https://api.coingecko.com/api/v3/simple/price?x_cg_demo_api_key={API_KEY_GECKO}"
    params = {
        "symbols": ids_str,
        "vs_currencies": "brl"
    }

    list_new_values = []

    res = requests.get(url, params=params)
    data = res.json()

    for ticker in df[TICKER_COL]:
        ticker = ticker.lower()
        if ticker in data and "brl" in data[ticker]:
            price = float(data[ticker]["brl"])
            list_new_values.append(price)
        else:
            list_new_values.append("Error")

        time.sleep(0.1)

    df_novo = df.copy()
    df_novo[VALUE_COL] = list_new_values

    return df_novo
    
def fetch_assets(df):
    df_assets_us = df[df[CURRENCY_BASE_COL] == "USD"]
    df_assets_global = df[df[CURRENCY_BASE_COL] != "USD"]
    if(len(df_assets_us) > 0):
        df_assets_us = fetch_assets_us(df_assets_us)
    if(len(df_assets_global) >0):
        df_assets_global = fetch_assets_global(df_assets_global)
    
    return pd.concat([df_assets_us, df_assets_global], ignore_index=True)

    
def convert_values_to_brl(df_assets, df_moedas):    
    map_moeda_valor = dict(zip(df_moedas[TICKER_COL], df_moedas[VALUE_COL]))
    
    df_result = df_assets.copy()
    df_result[VALUE_COL] = df_result[VALUE_COL] * df_result[CURRENCY_BASE_COL].map(map_moeda_valor)
    
    return df_result

def handle_get_currencies(df):
    df_currency_brl_only = df[(df[TYPE_COL] == "FIAT") & (df[TICKER_COL] == "BRL")]

    df_currencies_api = df[(df[TYPE_COL] == "FIAT") & (df[TICKER_COL] != "BRL")]
    df_currencies_api = fetch_currencies(df_currencies_api)

    return pd.concat([df_currencies_api, df_currency_brl_only], ignore_index=True)

def handle_get_assets(df_quote, df_currencies):
    df_assets_api = df_quote[(df_quote[TYPE_COL] != "FIAT") & (df_quote[TYPE_COL] != "CRIPTO")]
    df_assets_api = fetch_assets(df_assets_api)
    return convert_values_to_brl(df_assets_api, df_currencies)


def handle_get_criptos(df):
    df_criptos_api = df[df[TYPE_COL] == "CRIPTO"]
    return fetch_criptos(df_criptos_api)

# ********* Cotação *********
def start_flow_quote(wb, date_today):
    ws_quote = wb[SHEET_QUOTE_NAME]
    table_quote = ws_quote._tables[TABLE_QUOTE_NAME]
    header, table_quote_data = ler_tabela_para_dicionarios(ws_quote, table_quote)

    global DATE_COL, TICKER_COL, VALUE_COL, CURRENCY_BASE_COL, TYPE_COL

    # Mapeando Colunas
    DATE_COL= header[0]   
    TICKER_COL = header[1]
    VALUE_COL = header[2]
    CURRENCY_BASE_COL = header[3]
    TYPE_COL = header[4]

    # Transofrmando Table em DataFrame
    df = pd.DataFrame(table_quote_data)

    # Montando DataFrame de Insert ou Update
    latest_date = df[DATE_COL].max()
    df_quote = df[df[DATE_COL] == latest_date].copy()
    is_insert = False
    if(latest_date < pd.Timestamp(date_today)):
        df_quote[DATE_COL] = date_today
        is_insert = True

    # Chamadas Http para APIs
    df_currencies_api = handle_get_currencies(df_quote)
    df_assets_api = handle_get_assets(df_quote, df_currencies_api)
    df_criptos_api = handle_get_criptos(df_quote)

    # Inserindo Novos Dados
    df_new_quotes =  pd.concat([df_currencies_api, df_assets_api, df_criptos_api], ignore_index=True)
    upsert_table_excel_data(wb, ws_quote, table_quote, df_new_quotes, is_insert)

# ********* Investimento *********
def start_flow_investiment(wb, date_today):
    # Mapeando Tabela
    ws_investiment = wb[SHEET_INVESTIMENT_NAME]
    table_investiment = ws_investiment._tables[TABLE_INVESTIMENT_NAME]
    header, table_investiment_data = ler_tabela_para_dicionarios(ws_investiment, table_investiment)

    global DATE_COL, NAME_COL, INSTITUTION_COL, TYPE_COL, QUOTE_VALUE_COL, QUOTE_BASE_CURRENCY_COL, ASSET_COL, BASE_CURRENCY_COL, QTDE_COL, TOTAL_BRL_COL, TOTAL_USD_COL
    # Mapeando Colunas
    DATE_COL= header[0]   
    NAME_COL = header[1]
    INSTITUTION_COL = header[2]
    TYPE_COL = header[3]
    QUOTE_VALUE_COL = header[4]
    QUOTE_BASE_CURRENCY_COL = header[5]
    ASSET_COL = header[6]
    BASE_CURRENCY_COL = header[7]
    QTDE_COL = header[8]
    TOTAL_BRL_COL = header[9]
    TOTAL_USD_COL = header[10]

    # Transofrmando Table em Df
    df = pd.DataFrame(table_investiment_data)
    # Montando DataFrame de Insert ou Update
    latest_date = df[DATE_COL].max()
    df_investiment = df[df[DATE_COL] == latest_date].copy()

    if(latest_date < pd.Timestamp(date_today)):
        df_investiment[DATE_COL] = date_today

        # Inserindo Novos Dados
        upsert_table_excel_data(wb, ws_investiment, table_investiment, df_investiment, True)

def get_current_date_start_of_month():
    today = datetime.today()
    return date(today.year, today.month, 1)

# -------- Env Vars ---------
REF_COL = "Ref Cells"
# *** Cotação ***
SHEET_QUOTE_NAME = "Cotacoes"
TABLE_QUOTE_NAME = "Cotacoes_01"
API_KEY_ALPHA = "J9OM0X9200KP47G2"
API_KEY_GECKO = "CG-ayNYBkPDUfbHRwk4MbWVrYiE"
API_KEY_FINNHUB = "d3o1m79r01qmj82ve8jgd3o1m79r01qmj82ve8k0"
# *** Investimento ***
SHEET_INVESTIMENT_NAME = "Investimentos"
TABLE_INVESTIMENT_NAME = "Investimentos_01"

# -------- Main ---------
# Acessando Arquivo
clean_terminal()
try:
    EXCEL_PATH = get_excel_file()
    if (EXCEL_PATH == None):
        raise Exception("Nenhuma Planilha Encontrada!")
    nome_arquivo = EXCEL_PATH.rsplit("/", 1)[-1]
    password = getpass.getpass(f"Digite a senha da planilha, se houver ({nome_arquivo}): ")

    from openpyxl import load_workbook
    from openpyxl.utils import get_column_letter, range_boundaries
    import io
    import os
    import msoffcrypto
    import pandas as pd
    from datetime import datetime, date
    import requests
    import time
    import warnings
    from copy import copy
    import getpass
    from msoffcrypto.format.ooxml import OOXMLFile

    if(password == "" or password == None):
        wb = load_workbook(EXCEL_PATH, data_only=False)
    else:
        decrypted_workbook = open_workbook_with_password(EXCEL_PATH, password)
        wb = load_workbook(filename=decrypted_workbook)


    # Inciando Fluxos
    print("\n**** Inciando Atualização ****\n")
    date_today = get_current_date_start_of_month()

    start_flow_quote(wb, date_today)
    start_flow_investiment(wb, date_today)

    wb[SHEET_QUOTE_NAME]["A1"] = f"Última Atualização"
    wb[SHEET_QUOTE_NAME]["A2"] = f"{datetime.now():%d/%m/%Y %H:%M:%S}"

    # Salvando em Disco
    final_buf = io.BytesIO()
    wb.save(final_buf)
    final_buf.seek(0)
    if(password == "" or password == None):
        with open(EXCEL_PATH, "wb") as f_out:
            f_out.write(final_buf.getvalue())
    else:
        with open(EXCEL_PATH, "wb") as f_out:
            office = OOXMLFile(final_buf)
            office.encrypt(password, f_out)

    print("\n**** Atualização Concluída ****")

except Exception as e:
    print("\nHouve um erro:", e)