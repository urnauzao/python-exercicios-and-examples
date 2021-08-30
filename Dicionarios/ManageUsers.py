from Dicionarios.Funcoes import *
usuarios = {}

opcao = perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios)
    if opcao=="E":
        excluir(usuarios)
    if opcao=="L":
        listar(usuarios)
    opcao = perguntar()