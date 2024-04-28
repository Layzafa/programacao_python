import pandas as pd

dataFrame = pd.read_excel("Arquivos\Tratamento_Dados.xlsx")
print(dataFrame)

#preenchendo os valores vazios com a média da coluna total vendas
dataFrameValorMedio = dataFrame.fillna(dataFrame["Total Vendas"].mean())
print(dataFrameValorMedio)

#preencher os valores vazios com um valor fixo
dataFrameValorMedio = dataFrame.fillna(5)
print(dataFrameValorMedio)

#preencher os valores vazios com o último valor não vazio
dataFarmeUltimoValor = dataFrame.ffill()
print(dataFarmeUltimoValor)

#contando vendas do mês
dataFrameVendas = dataFrame["Vendedor"].value_counts()
print(dataFrameVendas)

#contando o total de vendas por vendedor
vendedor = dataFarmeUltimoValor.groupby("Vendedor").sum("Total Vendas")
print(vendedor)