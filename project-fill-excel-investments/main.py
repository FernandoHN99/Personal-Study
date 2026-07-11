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

    # Mapeando Colunas (por nome fixo, não por posição)
    DATE_COL = "Data"
    TICKER_COL = "Ticker"
    VALUE_COL = "Valor"
    CURRENCY_BASE_COL = "Moeda Base"
    TYPE_COL = "Tipo"

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
# DEPRECATED - agora usa xlwings no bloco principal
# def start_flow_investiment(wb, date_today, sheet_name, table_name):
#     # Mapeando Tabela
#     ws_investiment = wb[sheet_name]
#     table_investiment = ws_investiment._tables[table_name]
#     header, table_investiment_data = ler_tabela_para_dicionarios(ws_investiment, table_investiment)
#
#     # Transformando Table em DataFrame
#     df = pd.DataFrame(table_investiment_data)
#     
#     # Montando DataFrame de Insert ou Update
#     # Usa apenas a coluna "Data" para determinar se o mês virou
#     latest_date = df["Data"].max()
#     df_investiment = df[df["Data"] == latest_date].copy()
#
#     if(latest_date < pd.Timestamp(date_today)):
#         df_investiment["Data"] = date_today
#         # Inserindo Novos Dados
#         upsert_table_excel_data(wb, ws_investiment, table_investiment, df_investiment, True)

def get_current_date_start_of_month():
    today = datetime.today()
    return date(today.year, today.month, 1)

# -------- Funções xlwings ---------

def get_table_ranges(excel_path):
    """
    Descobre os ranges atuais das tabelas usando openpyxl (read-only).
    Retorna dict {table_name: "range_str"}
    """
    from openpyxl import load_workbook
    try:
        wb_ro = load_workbook(excel_path, data_only=False)
        ranges = {}
        for sheet_name in wb_ro.sheetnames:
            ws = wb_ro[sheet_name]
            for table_name in ws._tables:
                table_obj = ws._tables[table_name]
                table_ref = table_obj if isinstance(table_obj, str) else table_obj.ref
                ranges[table_name] = table_ref
        wb_ro.close()
        return ranges
    except Exception as e:
        print(f"Erro ao ler ranges das tabelas: {e}")
        return {}

def read_table_xlwings(sheet, table_range_str):
    """
    Lê uma tabela Excel usando xlwings e retorna header e dados como lista de dicts.
    table_range_str: ex "C4:G136" (header na primeira linha do range)
    """
    try:
        # Ler toda a range
        rng = sheet.range(table_range_str)
        all_data = rng.value
        
        if not all_data:
            return [], []
        
        # Se só tem 1 linha, retorna como tupla simples
        if not isinstance(all_data[0], (list, tuple)):
            all_data = [all_data]
        
        # Primeira linha é header
        header = all_data[0]
        data_rows = all_data[1:]
        
        # Converter para lista de dicts
        table_data = []
        for row in data_rows:
            row_dict = dict(zip(header, row))
            table_data.append(row_dict)
        
        return header, table_data
    except Exception as e:
        print(f"Erro ao ler tabela {table_range_str}: {e}")
        return [], []

def write_table_xlwings(sheet, table_range_str, df_data):
    """
    Escreve dados em uma tabela Excel usando xlwings (update na última leva).
    Encontra as últimas N linhas e atualiza seus valores.
    """
    try:
        # Parse range string (ex: "C4:G136" -> start_row=4, end_row=136)
        from openpyxl.utils import get_column_letter
        parts = table_range_str.split(':')
        start_cell = parts[0]  # Ex: "C4"
        end_cell = parts[1]    # Ex: "G136"
        
        import re
        start_match = re.match(r'([A-Z]+)(\d+)', start_cell)
        end_match = re.match(r'([A-Z]+)(\d+)', end_cell)
        
        start_col_letter = start_match.group(1)
        start_row_num = int(start_match.group(2))
        end_row_num = int(end_match.group(2))
        
        n_rows_to_update = len(df_data)
        n_data_rows = end_row_num - start_row_num  # sem contar o header
        
        # Atualizar as últimas N linhas de dados
        first_update_row = end_row_num - n_rows_to_update + 1
        
        for idx, (i, row) in enumerate(df_data.iterrows()):
            for col_idx, col_name in enumerate(df_data.columns):
                cell_address = f"{get_column_letter(ord(start_col_letter) - ord('A') + 1 + col_idx)}{first_update_row + idx}"
                sheet.range(cell_address).value = row[col_name]
    except Exception as e:
        print(f"Erro ao escrever na tabela {table_range_str}: {e}")

def insert_table_xlwings(sheet, table_range_str, df_data):
    """
    Insere novas linhas em uma tabela Excel usando xlwings.
    Escreve os dados nas linhas imediatamente após o range atual.
    """
    try:
        import re
        from openpyxl.utils import get_column_letter
        
        # Parse range (ex: "C4:G136" -> colunas de C a G, linhas 4 a 136)
        parts = table_range_str.split(':')
        start_cell = parts[0]
        end_cell = parts[1]
        
        start_match = re.match(r'([A-Z]+)(\d+)', start_cell)
        end_match = re.match(r'([A-Z]+)(\d+)', end_cell)
        
        start_col_letter = start_match.group(1)
        start_col_num = ord(start_col_letter) - ord('A')
        start_row_num = int(start_match.group(2))
        end_row_num = int(end_match.group(2))
        
        # Inserir dados começando da linha após o final do range
        first_new_row = end_row_num + 1
        
        for idx, (i, row) in enumerate(df_data.iterrows()):
            for col_idx, col_name in enumerate(df_data.columns):
                col_letter = get_column_letter(start_col_num + col_idx + 1)
                cell_address = f"{col_letter}{first_new_row + idx}"
                sheet.range(cell_address).value = row[col_name]
    except Exception as e:
        print(f"Erro ao inserir na tabela {table_range_str}: {e}")



# -------- Env Vars ---------
REF_COL = "Ref Cells"
# *** Cotação ***
SHEET_QUOTE_NAME = "Cotacoes"
TABLE_QUOTE_NAME = "Table_Cotacoes"
API_KEY_ALPHA = "J9OM0X9200KP47G2"
API_KEY_GECKO = "CG-ayNYBkPDUfbHRwk4MbWVrYiE"
API_KEY_FINNHUB = "d3o1m79r01qmj82ve8jgd3o1m79r01qmj82ve8k0"
# *** Investimento ***
SHEET_INVEST_MAIN = "Investimentos_Main"
TABLE_INVEST_MAIN = "Table_Investimentos_Main"
SHEET_INVEST_PORCENT = "Investimentos_Porcent"
TABLE_INVEST_PORCENT = "Table_Investimentos_Porcent"

# -------- Main ---------
# Acessando Arquivo
clean_terminal()
try:
    EXCEL_PATH = get_excel_file()
    if (EXCEL_PATH == None):
        raise Exception("Nenhuma Planilha Encontrada!")
    nome_arquivo = EXCEL_PATH.rsplit("/", 1)[-1]
    password = getpass.getpass(f"Digite a senha da planilha, se houver ({nome_arquivo}): ")

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
    import xlwings as xw

    if(password != "" and password != None):
        raise Exception("Senha de planilha não é suportada com xlwings. Abra a planilha sem senha.")
    
    # Abrir workbook com xlwings (Excel controla o arquivo)
    try:
        book = xw.Book(EXCEL_PATH)
    except Exception as e:
        raise Exception(f"Erro ao abrir planilha com xlwings. Certifique-se que o Excel está instalado e acessível: {e}")


    # Iniciando Fluxos
    print("\n**** Iniciando Atualização ****\n")
    date_today = get_current_date_start_of_month()
    
    # Descobrir ranges das tabelas
    table_ranges = get_table_ranges(EXCEL_PATH)
    quote_range = table_ranges.get(TABLE_QUOTE_NAME)
    invest_main_range = table_ranges.get(TABLE_INVEST_MAIN)
    invest_porcent_range = table_ranges.get(TABLE_INVEST_PORCENT)
    
    if not quote_range or not invest_main_range or not invest_porcent_range:
        raise Exception(f"Não conseguiu descobrir ranges das tabelas. Ranges encontrados: {table_ranges}")
    
    # *** COTAÇÕES ***
    ws_quote = book.sheets[SHEET_QUOTE_NAME]
    header_quote, data_quote = read_table_xlwings(ws_quote, quote_range)
    
    if header_quote:
        df_quote = pd.DataFrame(data_quote)
        latest_date = df_quote["Data"].max()
        df_quote_latest = df_quote[df_quote["Data"] == latest_date].copy()
        
        is_insert = False
        if latest_date < pd.Timestamp(date_today):
            df_quote_latest["Data"] = date_today
            is_insert = True
        
        # Atualizar colunas globais para as funções de fetch
        global DATE_COL, TICKER_COL, VALUE_COL, CURRENCY_BASE_COL, TYPE_COL
        DATE_COL = "Data"
        TICKER_COL = "Ticker"
        VALUE_COL = "Valor"
        CURRENCY_BASE_COL = "Moeda Base"
        TYPE_COL = "Tipo"
        
        # Chamadas HTTP para APIs
        df_currencies_api = handle_get_currencies(df_quote_latest)
        df_assets_api = handle_get_assets(df_quote_latest, df_currencies_api)
        df_criptos_api = handle_get_criptos(df_quote_latest)
        
        # Inserir/atualizar dados
        df_new_quotes = pd.concat([df_currencies_api, df_assets_api, df_criptos_api], ignore_index=True)
        
        if is_insert:
            insert_table_xlwings(ws_quote, quote_range, df_new_quotes)
        else:
            write_table_xlwings(ws_quote, quote_range, df_new_quotes)
    
    # *** INVESTIMENTOS ***
    for sheet_name, table_name, table_range in [(SHEET_INVEST_MAIN, TABLE_INVEST_MAIN, invest_main_range), (SHEET_INVEST_PORCENT, TABLE_INVEST_PORCENT, invest_porcent_range)]:
        ws_invest = book.sheets[sheet_name]
        header_invest, data_invest = read_table_xlwings(ws_invest, table_range)
        
        if header_invest:
            df_invest = pd.DataFrame(data_invest)
            latest_date = df_invest["Data"].max()
            df_invest_latest = df_invest[df_invest["Data"] == latest_date].copy()
            
            if latest_date < pd.Timestamp(date_today):
                df_invest_latest["Data"] = date_today
                insert_table_xlwings(ws_invest, table_range, df_invest_latest)
    
    # Atualizar timestamp
    ws_quote.range("A1").value = "Última Atualização"
    ws_quote.range("A2").value = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Salvar via Excel (preserva gráficos, slicers, etc)
    book.save()
    book.close()

    print("\n**** Atualização Concluída ****")

except Exception as e:
    print("\nHouve um erro:", e)