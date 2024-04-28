import pandas as pd

dataFrame = pd.read_excel("Arquivos\Base_Vendas.xlsx")
print(dataFrame)

#contando valores únicos
valoresunicos = dataFrame.nunique()
print(valoresunicos)

#verificar se o valor é duplicado
valorduplicado = dataFrame.duplicated(subset= "Vendedor", keep= False)
print(valorduplicado)
#keep= "first" aceita o primeiro como não duplicata
#keep= "last" aceita o último como não duplicata
#keep= False marca todas as instâncias que têm duplicata

#criando uma coluna no dataFrame
dataFrame["Confere Duplicidade"] = dataFrame.duplicated(subset= "Vendedor", keep= "first")
print(dataFrame)

#remover  duplicatas
removerDuplicatas = dataFrame.drop_duplicates(subset= "Vendedor", keep= "first")
print(removerDuplicatas)
