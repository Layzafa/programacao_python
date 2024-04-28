import pandas as pd

#https://docs.google.com/spreadsheets/d/1eIRK5LkL6GrYSDWyyuGMVdV9wDBapQeiNUDJjMB7f_g/edit?usp=sharing

planilha_id = "1eIRK5LkL6GrYSDWyyuGMVdV9wDBapQeiNUDJjMB7f_g"
dataFrame = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{planilha_id}/export?format=csv")

dataFrame = dataFrame.drop(columns= ["Produto", "Data Venda"])

dataFrame["Total Vendas"] = dataFrame["Total Vendas"].replace({',':'.'}, regex= True). astype(float)

dataFrame = dataFrame.groupby("Vendedor").sum()
print(dataFrame)

dataFrame.to_csv("Desafio1.csv", index= True)
