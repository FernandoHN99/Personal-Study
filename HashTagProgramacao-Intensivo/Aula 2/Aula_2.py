import pandas as pd
import plotly.express as px

# Acessando a Base de Dados
tabela = pd.read_csv(r'C:\Users\fernando.h.neto\Downloads\microsoft.microsoftskydrive_8wekyb3d8bbwe!App\Downloads\Intensivo Python\Aula 2\telecom_users.csv')

# Tratando base de dados

# Jogando fora uma coluna pelo nome
tabela = tabela.drop('Unnamed: 0', axis=1)  # axis = 1 -> | Coluna axis = 0 -> Linha
# Transformando uma coluna de string (object) para numeric (float64) 
tabela['TotalGasto'] = pd.to_numeric((tabela['TotalGasto']), errors='coerce')
# Apagando valores vazios
tabela = tabela.dropna(how='all', axis=1) # exclui qualquer coluna que tenha todos os valores vazios
tabela = tabela.dropna(how='any', axis=0) # exclui qualquer linha que tenha algum valor vazio
# print(tabela)
# print(tabela.info())

# Criação das variáveis para análise inicial
qtdChurn = tabela["Churn"].value_counts() # Variavel tipada de número de pessoas que cancelaram a assinatura
qtdChurnPorcent = tabela["Churn"].value_counts(normalize=True) # Variavel tipada de procentagem em decimal de pessoas que cancelaram a assinatura
# print(qtdChurn)
# print(qtdChurnPorcent)

# Criação dos gráficos para análise detalhada
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn') # Monta um gráfico desse tipo divindo pela coluna e ainda evidenciando dentro disso se o cara cancelou (Churn) ou não
    grafico.show()
