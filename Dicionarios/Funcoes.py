def perguntar():
 return input(
    "O que deseja realizar?\n"+
    "<I> - Para Inserir um novo usuário\n"+
    "<P> - Para Pesquisar um usuário\n"+
    "<E> - Para Excluir um usuário\n"+
    "<L> - Para Listar os usuários\n"+
    "Digite a letra da opção desejada: \n"
).upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
            input("Digite a última data de acesso: "),
            input("Qual a última estação acessada: ").upper()
        ]
def pesquisar(dicionario):
    print(dicionario[input("Qual o login do usuário?").upper()])

def excluir(dicionario):
    del(dicionario[input("Qual o login do usuário a ser REMOVIDO?").upper()])
    listar(dicionario)

def listar(dicionario):
    print("\n ### Lista de usuários:")
    for elemento in dicionario:
        print("Login:", elemento, " | Nome: ", dicionario[elemento][0], " | Último acesso: ", dicionario[elemento][1], " | Local: ", dicionario[elemento][2])
        # print(elemento, dicionario[elemento])