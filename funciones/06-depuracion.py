def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("breakpoint")
l = largo("Hola")
print(l)
