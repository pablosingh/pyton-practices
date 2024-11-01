import math

n1 = input("Ingresa el 1er numero ")
n2 = input("Ingresa el 2do numero ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2

mensaje = f"""
Para los números {n1} y {n2}
La suma es {suma}
La resta es {resta}
La multiplicación es {multi}
La división es {divi}
"""
print(mensaje)
