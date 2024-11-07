#  sets son grupos o conjuntos // NO se pueden REPETIR
# No podemos acceder a los elementos de esto

primero = {1, 1, 1, 2, 3, 3, 4}  # {1, 2, 3, 4}
print(primero)

# primero.add(5)
# primero.remove(2)
# print(primero)

segundo = [3, 4, 5, 6]
segundo = set(segundo)  # {3, 4, 5, 6}
print(segundo)

print("Union", primero | segundo)  # Hace una UNION
print("Interseccion", primero & segundo)  # Hace una UNION
print("Diferencia", primero - segundo)  # Hace una UNION
print("Diferencia Simetrica", primero ^ segundo)  # Hace una UNION

# print(segundo[0]) Da error

if 5 in segundo:
    print("Si se encuentra")
else:
    print("No se encuentra")
