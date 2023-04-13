import pandas as pd                                     # Mexer com base de dados
import matplotlib.pyplot as plt                         # Plotar o gráfico
import seaborn as sns                                   # Criar o gráfico
from sklearn.model_selection import train_test_split    # Divide a massa de dados para treino e teste
from sklearn.linear_model import LinearRegression       # Cria IA de Regressão Linear
from sklearn.ensemble import RandomForestRegressor      # Cria IA de Árvore de Previsão
from sklearn import metrics                             # Faz o cálculo de precisão das IA's


# Coletando a base de dados
tabela = pd.read_csv(r'C:\Users\fernando.h.neto\Downloads\microsoft.microsoftskydrive_8wekyb3d8bbwe!App\Downloads\Intensivo Python\Aula 4\advertising.csv')
# print(tabela)
# print(tabela.info())

# Criando um mapa de calor
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True) # cmap=Padrão de cores e annot=anotações dentro de cada bloco
# plt.show()

# Separando a base de dados em x e y
x = tabela[['TV', 'Radio', 'Jornal']] # quem eu USO para prever
y = tabela['Vendas'] # quem eu QUERO prever

# Separando a base de dados em dados de treino e dados de teste
xTreino, xTeste, yTreino, yTeste = train_test_split(x,y) #train_test_split(x,y, test_size = 0.3) você decide porcent de teste

# Criando duas inteligências artificiais
modelRegressionLinear = LinearRegression()
modelForestDecision = RandomForestRegressor()

# Treinando as inteligências artificiais
modelRegressionLinear.fit(xTreino, yTreino)
modelForestDecision.fit(xTreino, yTreino)

# Descobrindo o melhor modelo com a massa de teste (xTeste, yTeste)
# Testando efetivamente (xTeste)
privisaoRegressionLinear = modelRegressionLinear.predict(xTeste)
privisaoForestDecision = modelForestDecision.predict(xTeste)

# Comparando com os resultados reais (yTeste)
r2Regression = metrics.r2_score(yTeste, privisaoRegressionLinear)
r2forest = metrics.r2_score(yTeste, privisaoForestDecision)
print(f'Regression - R²: {r2Regression}')
print(f'Forest - R²: {r2forest}')

tabelaAuxilar = pd.DataFrame()
tabelaAuxilar['yTeste'] = yTeste
tabelaAuxilar['Previsao Arvore Decisao'] = privisaoForestDecision
tabelaAuxilar['Previsao Regressão Linear'] = privisaoRegressionLinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabelaAuxilar)
# plt.show()

# Importar uma nova tabela para Previsão
tabelaPrevision = pd.read_csv(r'C:\Users\fernando.h.neto\Downloads\microsoft.microsoftskydrive_8wekyb3d8bbwe!App\Downloads\Intensivo Python\Aula 4\novos.csv')
# print(tabelaPrevision)

previsao = modelForestDecision.predict(tabelaPrevision)
print(previsao)
