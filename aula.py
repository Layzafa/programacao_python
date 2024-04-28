import pandas as pd
import matplotlib.pyplot as plt
dataFrameJogos14_22 = pd.read_csv("games.csv")
#Traduzindo colunas
colunas = ["Data da Partida", "ID Partida", "Estado da Partida", "ID Time da Casa", "ID Time Visitante", 
           "Temporada", "ID_Time_da_Casa", "Pontos Casa", "Porcentagem Pontos de 2 Casa", "Porcentagem Lançes livres Casa", 
           "Porcentagem Aremessos de 3 Casa", "Porcentagem Assitencia Casa", "Porcentagem Rebotes Casa", "ID_Time_Visitante", 
           "Pontos Visitante", "Porcentagem Pontos de 2 Visitante", "Porcentagem Lançes livres Visitante", 
           "Porcentagem Aremessos de 3 Visitante", "Porcentagem Assitencia Visitante", "Porcentagem Rebotes Visitante", 
           "Vitória do Time da Casa"]
dataFrameJogos14_22.columns = colunas
#print(dataFrameJogos14_22)

#Removendo Colunas Inuteis
dataFrameJogos14_22 = dataFrameJogos14_22.drop(columns=["Estado da Partida","ID_Time_da_Casa","ID_Time_Visitante"])
#print(dataFrameJogos14_22)

#Alterando o ID do time pelo nome
dataFrameTimes = pd.read_csv("teams.csv") #Transformando o dataset teams.csv em dataframe
dataFrameNomesID = dataFrameTimes.loc[:,["TEAM_ID","NICKNAME"]] #Pegando somente as colunas TEAM_ID e NICKNAME
#print(dataFrameNomesID)

#Alterando o tipo das colunas do dataFrame principal para poder fazer o replace()
dataFrameJogos14_22["ID Time da Casa"] = dataFrameJogos14_22["ID Time da Casa"].astype(str)
dataFrameJogos14_22["ID Time Visitante"] = dataFrameJogos14_22["ID Time Visitante"].astype(str)

#Usando um loop para poder percorrer todos os valores das colunas TEAM_ID e NICKNAME de dataFrameNomesID
for x in range((dataFrameNomesID.size//2)):
    id = str(dataFrameNomesID.loc[x]["TEAM_ID"])
    nome = str(dataFrameNomesID.loc[x]["NICKNAME"])
    #Depois de pegar os valores ID e NOME de uma linha respectiva o replace vai trocar todos os IDS pelo NICKNAME de todo o dataframe
    dataFrameJogos14_22["ID Time da Casa"] = dataFrameJogos14_22["ID Time da Casa"].replace(id, nome)
    dataFrameJogos14_22["ID Time Visitante"] = dataFrameJogos14_22["ID Time Visitante"].replace(id, nome)

#Mostrando os valores alterados das colunas
print(dataFrameJogos14_22.loc[:,["ID Time da Casa","ID Time Visitante"]])

#Salvando arquivo
dataFrameJogos14_22.to_csv("resultado.csv", encoding='utf-8', index=False, sep=',')

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Comparando Desempenho de Times Especificos Estando Dentro e Fora de Casa

#Mostrando Quantidade de Vitorias - Casa e Fora
vitoriasTimes = dataFrameJogos14_22.loc[:,["ID Time da Casa", "Vitória do Time da Casa"]]
vitoriasTimes.columns = ["Nome Time", "Vitórias"]
vitoriasTimes = vitoriasTimes.groupby("Nome Time").sum()
#Criando plot
vitoriasTimes.plot(title="Total de Vítorias Times", legend=True, xlabel="Time", ylabel="Quantidade Vitórias")

#Pegando valores pras temporadas pra organizar o xticks das figuras.
temporadas = []
for x in dataFrameJogos14_22["Temporada"].unique():
    temporadas.append(x)

time = "Warriors"

#Mostrando Média de Pontos De Time Especifico - Casa e Fora
timesMédiaP = dataFrameJogos14_22.loc[:,["ID Time da Casa","Temporada","Pontos Casa", "Pontos Visitante"]]
timesMédiaP.columns = ["Time", "Temporada", "Pontos em Casa", "Pontos como Visitante"]
timesMédiaP = timesMédiaP.groupby(["Time","Temporada"]).mean()
timeWarriorsP = timesMédiaP.loc[time,:]
#Criando a figura
timeWarriorsP.plot(title=f"{time}",xticks=temporadas)

#Mostrando Porcentagem Média de Rebotes - Casa e Fora
timesMédiaR = dataFrameJogos14_22.loc[:,["ID Time da Casa","Temporada", "Porcentagem Rebotes Casa", "Porcentagem Rebotes Visitante"]]
timesMédiaR.columns = ["Time", "Temporada", "Porcentagem Rebotes em Casa", "Porcentagem Rebotes como Visitante"]
timesMédiaR = timesMédiaR.groupby(["Time","Temporada"]).mean()
timeWarriorsR = timesMédiaR.loc[time,:]
#Criando a figura
timeWarriorsR.plot(title=f"{time}",xticks=temporadas)

#Mostrando Porcentagem Média de Assitencias - Casa e Fora
timesMédiaA = dataFrameJogos14_22.loc[:,["ID Time da Casa","Temporada", "Porcentagem Assitencia Casa", "Porcentagem Assitencia Visitante"]]
timesMédiaA.columns = ["Time", "Temporada", "Porcentagem Assistências em Casa", "Porcentagem Assistências como Visitante"]
timesMédiaA = timesMédiaA.groupby(["Time","Temporada"]).mean()
timeWarriorsA = timesMédiaA.loc[time,:]
#Criando a figura
timeWarriorsA.plot(title=f"{time}",xticks=temporadas)



#Mostrando figuras
plt.show()