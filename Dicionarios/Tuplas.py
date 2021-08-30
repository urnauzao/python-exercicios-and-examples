usuarios = {} #lista
emails  = ["xpto@xyz.com", "xkcd@phd.com", "tester@teste.com"] #dicionário

tupla = list(enumerate(emails)) #tupla
print("Tupla:", tupla, "\n ---- \n")

for chave in range(0, len(tupla)): #len = tamanho da tupla - 1
    print ("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome: "), input("Digite o nível:")]

print("Usuarios:", usuarios, "---- \n")

# for (chave, dado) in usuarios.items():
for chave, dado in usuarios.items():
    print("Usuario.: ", chave[0])
    print("Email...: ", chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])
