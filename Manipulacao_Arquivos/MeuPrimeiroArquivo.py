# Modos de Escrita no Arquivo
## a -> append
## r -> read
## w -> writew

# Modo 1
#arquivo = open("primeiro_arquivo.txt", "w")
#arquivo.write("Meu primeiro arquivo!")
#arquivo.close()

# Modo 2
# with fecha o arquivo assim que acaba o bloco
with open("../Files/primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nHakuna Matata!!")