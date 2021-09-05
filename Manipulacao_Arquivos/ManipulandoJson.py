import json

with open("../Files/characters_breaking_bad.json", "r") as arq_json:
    dicionarioFull = json.load(arq_json)
    dicionario = dicionarioFull['characters']
    for dados in dicionario:
        print(str(dados['char_id']) + " | " + dados['name'])