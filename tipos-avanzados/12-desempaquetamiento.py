lista = (1, 2, 3, 4)

lista2 = [5, 6, 7]

combinada = [*lista, "hola", *lista2]
print(combinada)

punto1 = {"x": 25, "y": 10}
punto2 = {"z": 15}

nuevoPunto = {**punto1, **punto2, "lala": "hola"}
print(nuevoPunto)
