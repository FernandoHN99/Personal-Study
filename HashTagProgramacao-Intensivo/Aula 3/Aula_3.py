from selenium import webdriver as web
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

def accessSearchGoogle(navegador, listXPATHSearch, whatToSearch):
    navegador.get('https://www.google.com.br/')
    for i, XPATH in enumerate(listXPATHSearch):
        try:
            navegador.find_element(By.XPATH, XPATH).send_keys(whatToSearch)
            navegador.find_element(By.XPATH, XPATH).send_keys(Keys.ENTER)
        except:
            if(i == listXPATHSearch.__sizeof__()): 
                navegador = navegador.close()       

                                                    # Abrindo o navegador
navegador = web.Chrome() # web.Chrome('chromedriver.exe') -> qdo chromedriver estiver no mesmo local do arquivo .py do vscode
listSearch = [ '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div/div[2]/input']


                                            # Pesquisando e Coletando informações do Dolar

accessSearchGoogle(navegador, listSearch, 'cotação dolar')
if navegador != None:
    cotacaoDolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


                                            # Pesquisando e Coletando informações do Euro
    accessSearchGoogle(navegador, listSearch, 'cotação euro')
    
    if navegador != None:
        cotacaoEuro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

                                            # Pesquisando e Coletando informações do Ouro
        navegador.get('https://www.melhorcambio.com/ouro-hoje')
        cotacaoOuro = navegador.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute('value')
        cotacaoOuro = cotacaoOuro.replace(',', '.')

if navegador != None:
    navegador.close() # Fechando o navegador

    # Importando base de dados
    tabela = pd.read_excel(r'C:\Users\fernando.h.neto\Downloads\microsoft.microsoftskydrive_8wekyb3d8bbwe!App\Downloads\Intensivo Python\Aula 3\Produtos.xlsx')

    # Editando a base de dados

    # Atualizando cotações
    tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacaoDolar)
    tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacaoEuro)    # { tabela.loc[linha, coluna] = Valor
    tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacaoOuro)

    # Atualizando Colunas da Tabela
    tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']
    tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

    # Exportando a minha base de dados
    tabela.to_excel('Produtos Novo.xlsx', index=False)
    print('Arquivo Criado com Sucesso!')