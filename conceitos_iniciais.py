# Tipos de variáveis

int #inteiro
float #decimal

# Operadores lógicos

+ # soma
- # subtração
/ # divisão
** # potenciação

# Funções

type()
input()
print()

# 'conjunto de caracteres' = string

'Uma string em Python'
 
len() # calcula a tamanho da string
print('\n') 
# ou
print("\t")

# Indexação

s = 'Hoje é segunda'
print(0) # printa o primeiro elemento da string
print(-1) # printa o ultimo elemento da string
print(:) # printa toda a string
print(0:2) # printa do primeiro elemento até o segundo elemento da string

# Indexação por espaçamento

print(::2) # printa os elementos num intervalo de dois em dois
print(::-1) # printa os elementos da string de trás para frente

# propriedades de strings
# Sao imultaveis
# Pode concatenar
s + ', droga' = 'Amanha é segunda, droga'

# funcoes proprias de strings
s.split() # separa os objetos da string
s.split(',') # separa a partir de um parametro, nesse caso, a virgula

# formatacao de impressao

.replace()

s = 'hoje'
print('String: %s' %(s)) # %s = string

# ou

s = 123
print('String: %r' %(s)) # %r = repr

# ou

s = 'a{x} b{y} c{z}'.format(x = 1, y = 'string', z = 3)
print(s)

# listas // tipo o array em C// é uma estrutura de dados em Python que acessa os dados a partir de indexação, isto é, posição relativa.
# Em Python não é preciso pré-definir o tamanho dos valores, pode ser alterado quando convir
# As listas podem ser concatenadas
# Podem ser operadas com soma, multiplicação
# Lista é ordenada, pois é acessado os dados a partir de sua posição

lista = [1, 2, 3, 4, 5]

# ou 

lista_dois = [1, 2, 'três', 4, 5]

lista + lista_dois # Une as duas listas
lista.append('6') # [1, 2, 3, 4, 5, 6]
lista.pop() # deleta o último objeto da lista ou o objeto especificado no parâmetro
lista * 10 # repete 10 vezes a lista
lista.sort() # ordena a lista
lista.reverse() # inverte a lista
lista[::-1] # Inverte a lista como o .reverse(), mas utlizanfo indexação

# Matriz
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

matriz = [lista1, lista2, lista3] # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Pode acessar o elemento da matriz assim:

matriz[0,1] # matriz[0,1] = 2

# ou 

matriz_linha = [row[0] for row in matriz] # Aqui itera o row(linha) para encontrar os valores da linha 0 "(row[0])"
# Isso é o mesmo que matriz = [matriz[0][0], matriz[1][0], matriz[2][0]]

# Dicionários // é uma estrutura de dados em python, a diferença é que a forma de acessar os dados não é por indexação, como nas listas, mas por mapeamente, isto é, acessa por uma chave. 
# Um dicionário não é ordenada nem sequenciado

my_dict = {'chave1':12, 'chave2':'string', 'chave3':[1, 2, [3, 4]]}

#para consultar o objeto no dicionário, utiliza a chave:
my_dict['chave1'] # vai printar o 12

my_dict['chave3'] # vai printar a lista e a partir dela podemos iterar os elementos e ir consultando os elementos da lista:

my_dict['chave3'][2] # printa [3, 4]
my_dict['chave3'][2][1] # printa 3
my_dict['chave3'][2][0] # printa 3
my_dict['chave3'][2][1] # printa 3

.upper() # printa os elementos em caixa preta

# posso criar um dicionário e ir adicionando os elementos adiante:

s = {}
s['chave'] = 'dog'

# consultar o dicionário:

my_dict.keys() # retorna as chaves e os elementos no dicionário e pode ser iterado para ir acessando cada chave:
# transformar em lista para iterar e consultar o dicionário:

list(my_dict.keys())[0] # printa chave1

# acessar os valores do dicionário:

my_dict.values()

# Tuplas são imultáveis e se assemelham a listas
# Aceitam vários tipos de dados diferentes
# É mais utilizada quando se quer manter a integridade dos dados

t = (1, 1, 1, 'string', 3, [4, 5, 6])

t.count(1) # retorna a quantidade de vezes repetidas do elemento dado, logo: 3.

t.append(7) # NÃO PODE SER ALTERADA UMA TUPLA, LOGO ESSA FUNÇÃO NÃO É POSSÍVEL!

t.index('string') # retorna o índice desse valor, no caso, 3.

# Leitura de arquivos

file = open('texto.txt') # Abrir um arquivo 
file.read() # Ler o arquivo
file.seek(0) # Inicia a leitura a partir do 0, analogia a um cursor com as posições relativas
file.readline() # Ler cada linha do arquivo

# %%writefile texto.txt >> um comando jupyter para criar um arquivo

# Laço

for line in file:  #o arquivo file é iterado e chama cada linha de 'line' ou qualquer outro nome (...)
    print(line) ## printa as linhas existentes no arquivo


# Sets >> conjunto de dados com valores únicos

numbers = set()

numbers.add(7, 7) # adiciona o valor ao conjunto 'numbers', contudo, apenas um valor, pois não pode adicionar valores duplicados.

x = [8, 8, 8, 11, 11, 2, 3, 4, 4]
set_x = set(x) # o resultado será: [2, 3, 4, 8, 11]

# Booleanos >> valores de verdade ou falso

a = True
b = False

# OPERADORE DE COMPARAÇÃO

1 == 1
1 != 2
1 < 2
2 > 1
1 <= 2
2 >= 1

# OPERADORES EM CADEIA

1 == 1 or 1 != 1 # True

1 == 1 and 1 != 1 # False

# Decisão

if a > b:
    print(a)
elif a == b:
    print(a)
else:
    print(b)

# Loops
# for - iterável

l = [1, 2, 3, 4, 5]
for n in l:
    print(n)

# While - iterável
num = 1
while num < 50:
    print(num + 1)

Range() #Cria listas com valores pré-definidos, é um tipo de gerador, objeto em python que itera e guarda na memória para ir acessando com o tempo;

for i in range(0, 10):
    print(i)

range(0, 30, 1) # Printa do 0 ao 29
range(30, 0, -1) # Printa na ordem decrescente até o 29
range(0, 30, 2) # Printa os números em ordem crescente num intervalo de dois em dois











