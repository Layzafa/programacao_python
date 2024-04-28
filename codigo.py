import pandas as pd
import numpy as np

#criar uma série
data = [10, 20, 30, 40, 50]
serie = pd.Series(data)
print(serie)

#criar uma lista de datas a partir da data 2024/01/01
listaData = pd.date_range("20240101", periods=31, freq="D")
print(listaData)

dataMeses = pd.date_range("20240101", periods=12, freq="M")
print(dataMeses)

#criar uma data frame com números aleatórios com numpy
numeros = pd.DataFrame(np.random.rand(5,1))
print(numeros)

#data frame números inteiros
inteiros = pd.DataFrame(np.random.rand(5,1)*10)
print(inteiros)

dataframe = pd.DataFrame(np.random.rand(15,3)*10, columns=["A", "B", "C"])
print(dataframe)

#data frame baseado em dicionário
x = {"Nome": ["João", "Maria", "Pedro", "Joana", "Vivian"], "Idade": [17,18,13,15,22]}
idadePessoas = pd.DataFrame(x)
print(idadePessoas)

#adicinar uma coluna
Sexos = ["M", "F", "M", "F", "F"] 
idadePessoas["sexos"] = Sexos
print(idadePessoas)

#visualizar colunas do data frame
print(idadePessoas.columns)

#vizualizar uma linha específica
print(idadePessoas.loc[1])

#vizualizar os dados de uma coluna
print(idadePessoas["sexos"])

#pegar valores de uma linha específica
print(idadePessoas.loc[0, ["Nome", "Idade"]])

#pegando valores específicos
print(idadePessoas.iloc[0,2])

#vizualizar os dados de cima para baixo
print(idadePessoas.head(2))

#vizualizar os dados de baixo para cima
print(idadePessoas.tail(2))

#vizualizar por periodo
print(idadePessoas.iloc[:,0:2])
#dois pontos sozinho para selecionar tudo

print(idadePessoas.iloc[0:2,:])

#usar valores booleanos para filtrar os dados
print(idadePessoas[idadePessoas["Idade"] >= 20])

#vizualiazar a partir do conteúdo dentro
print(idadePessoas[idadePessoas["Nome"].isin(["João", "Pedro"])])





