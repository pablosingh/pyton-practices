punto = {"x": 1, "y": 2, "z": 3}

for llave in punto:
    print(llave, punto[llave])

for tuplas in punto.items():
    print(tuplas)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Pablo"},
    {"id": 2, "nombre": "Roberto"},
    {"id": 3, "nombre": "Manuel"},
    {"id": 4, "nombre": "Singh"}
]

for usuario in usuarios:
    print(usuario["nombre"])
