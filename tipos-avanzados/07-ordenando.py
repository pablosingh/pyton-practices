numeros = [33, 5, 7, 3, 15, 25]
# numeros.sort()
# print(numeros)
# numeros.sort(reverse=True)
# print(numeros)

print(sorted(numeros, reverse=True))
print(numeros)

usuarios = [
    ["Pablo", 5],
    ["Mateo", 1],
    ["Roberto", 7]
]


def ordena(usuarios):
    return usuarios[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)

usuarios.sort(key=lambda elemento: elemento[1])
# lambda parametros: retorno
print(usuarios)
