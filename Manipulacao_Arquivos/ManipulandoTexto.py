texto = "Leia e Han Solo"
        #012345678901234
        #543210987654321 - (negativo)

#leia
print(texto[0:4])

# han solo (até o fim)
print(texto[7:])

# han solo (da posicao -8 até 0)
print(texto[-8:])

# inverter a string
# oloS naH e aieL
print(texto[::-1])

# pula de 2 em 2
# Li  a oo
print(texto[::2])

# text[ posicao inicial : quantidade de informação a percorrer : passo ]