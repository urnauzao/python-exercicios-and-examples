basedado = []
with open("../Files/iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedado.append(registro.split(","))
print(basedado)

# forçar ser float
print(float(basedado[0][0]) + float(basedado[0][1]))
