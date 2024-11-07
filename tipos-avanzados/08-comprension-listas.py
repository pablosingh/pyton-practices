usuarios = [
    ["Pablo", 5],
    ["Roberto", 7],
    ["Mateo", 1],
    ["Sebastian", 9]
]

# nombres = [expression for item in items]

# Transformar o Mapear
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)

# Map y Filter
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 1]
# print(nombres)

# nombres = list(map(lambda usuario: usuario[0], usuarios))

# nombres = list(filter(lambda usuario: usuario[1] > 5, usuarios))
# nombres = list(filter(lambda usuario: usuario[1] > 5, usuarios))
# nombres_solos = list(map(lambda nombre: nombre[0], nombres))

nombres_solos = list(map(lambda user: user[0], filter(
    lambda usuario: usuario[1] > 5, usuarios)))
print(nombres_solos)
