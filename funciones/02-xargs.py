def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(5, 2, 5, 7)
