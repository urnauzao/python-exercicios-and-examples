#definindo novo array
usuarios  = {}
print(usuarios)

#setando array
usuarios = {
    "chaves" : ["Chaves do 8", "24/12/20170", "Recep_01"],
    "quico" : ["Quico das Flores", "20/12/2017", "Raiox_03"]
}
print(usuarios)

#adicionar novo valor ao array
usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]
print(usuarios)

#pegar um ususario
print("Dados: ", usuarios.get('quico'))
