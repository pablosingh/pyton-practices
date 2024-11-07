numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple(numeros[:2])
print(punto)

# Se pueden hacer todas las operaciones que se realizan con las listas
# EXCEPTO MODIFICARLAS

primero, *otros, ultimo = numeros
print(primero)
print(otros)
print(ultimo)

for j in numeros:
    print(j)
