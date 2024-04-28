import pandas as pd

dataFrame = pd.read_excel("Arquivos\Deletar_Linhas_Colunas.xlsx")
print(dataFrame)

#remover linhas com valores vazios
dataFrame = dataFrame.dropna()
print(dataFrame)

#deletar linhas
del dataFrame["Produto"]
print(dataFrame)

#deletar mais de uma coluna
dataFrame = dataFrame.drop(columns=["Data Venda"])
#print(dataFrame)

#deletando linha 3 e 4
x = dataFrame.drop(2,axis=0)#linha, eixo
#axis = 0 - lihna; axis = 1 - coluna
print(dataFrame)


