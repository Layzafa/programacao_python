import psycopg2 #pip install psycopg2
#biblioteca que permite interagir com o postgres


def conectar_bd(): #Função que conecta com o BD
    try:
        conexao = psycopg2.connect( #Armazena todas as informações de conexão na variavel conexão
            dbname = "Cinema", #Nome do banco
            user = "postgres", #Usuario do postgres
            password = "postgres", #Senha do postgres
            host = "localhost" #Se estiver rodando local, localhost
        )
        print("Conectou no postgres!!!!") #mensagem de sucesso
        return conexao #permite que conexão possa interagir com o resto do código
    except psycopg2.Error as erro: #Caso haja um erro, vai imprimir
        print("Erro ao conectar: ",erro)
        return None
    
def listar_filme(conexao):
    try:
        cur = conexao.cursor() #Cria um cursor que é responsável por interagir com o banco e chama de cur
        cur.execute("SELECT * FROM filmes") #O cur executa o select
        filmes = cur.fetchall() #armazena todos os filmes dentro de um Array
        print("\nFILMES:")
        for filme in filmes: #percorre filme a filme, coluna por coluna
            print(f"ID:{filme[0]}| Titulo:{filme[1]} | Diretor: {filme[2]} | Gênero: {filme[3]} | Duração: {filme[4]} minutos")
    except psycopg2.Error as erro:#Caso haja um erro, vai imprimir
        print("Erro ao listar os filmes: ",erro)
    finally: #Encerra o cursor para evitar problemas
        cur.close()

def inserir_filme(conexao,titulo,diretor,genero,duracao): # Função que realiza a inserção na tabela filmes
    try:
        cur = conexao.cursor() #Cria o cursor 
        cur.execute("INSERT INTO filmes (titulo,diretor,genero,duracao_minutos) values (%s,%s,%s,%s)",(titulo,diretor,genero,duracao))
        # faz a insercao com os parametros passados
        conexao.commit() #salva as informações
        print("FIlme inserido!")
    except psycopg2.Error as erro:#Caso haja um erro, vai imprimir
        conexao.rollback() #desfaz a insersão caso haja erros
        print("Erro ao inserir filme: ",erro)
    finally:
        cur.close() #encerra o cursor

def criar_cliente(conexao,nome,email,telefone): #Função para criar clientes
    # Funciona da mesma maneira do inserir_filme
    try:
        cur= conexao.cursor()
        cur.execute("INSERT INTO clientes (nome,email,telefone) values(%s,%s,%s)",(nome,email,telefone))
        conexao.commit()
        print("Cliente Criado com sucesso")
    except psycopg2.Error as erro:#Caso haja um erro, vai imprimir
        conexao.rollback()
        print("Erro ao inserir cliente: ",erro)
    finally:
        cur.close()
        
def listar_clientes(conexao): #Funciona semelhante ao listar_filme
    try:
        cur = conexao.cursor()
        cur.execute("SELECT * FROM clientes")
        clientes = cur.fetchall()
        print("\nClientes")
        for cliente in clientes:
            print(f"|ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | Telefone: {cliente[3]}")
    except psycopg2.Error as erro:#Caso haja um erro, vai imprimir
        print("Erro ao listar o cliente")
    finally:
        cur.close()

def menu(): #Cria um menu para interagrir
    conexao = conectar_bd() #faz a conexão
    if conectar_bd == None: #Verifica se a conexão deu certo
        return

    #Exibe as opções
    while True:
        print("\nMENU INTERATIVO")
        print("1. Inserir Filme")
        print("2. Listar Filmes")
        print("3. Criar Cliente")
        print("4. Listar Clientes")
        print("5. Sair")
        opcao = int(input("Escolha uma opção: "))
        
        #Pede as informações e realiza a a função inserir_filme
        if opcao == 1:
            titulo = input("Digite o titulo do filme: ")
            diretor = input("Qual é o diretor do filme? ")
            genero = input("Digite o genero do filme: ")
            duracao = input("Digite a duração do filme em minutos: ")
            inserir_filme(conexao,titulo,diretor,genero,duracao)
        elif opcao == 2: #Mostra todos os filmes
            listar_filme(conexao)
        #Pede as informações e realiza a função criar_cliente
        elif opcao == 3:
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            criar_cliente(conexao, nome, email, telefone)
        elif opcao == 4:#Mostra todos os clientes
            listar_clientes(conexao)
        elif opcao ==5:
            break
        else:
            print("Opção inválida")
    conexao.close() #Ecerra a conexão
    print("Programa encerrado")
    
if __name__ == "__main__":
    menu() #Executa o menu