def elimina_espacios(texto):
    sin_espacios = ""
    for char in texto:
        if char != " ":
            sin_espacios += char
    # print(sin_espacios)
    return sin_espacios


def reverse(texto):
    invertido = ""
    for char in texto:
        invertido = char + invertido
    return invertido


def es_palindromo(texto):
    texto_sin_espacios = elimina_espacios(texto)
    invertido = reverse(texto_sin_espacios)
    return texto_sin_espacios.lower() == invertido.lower()


print("amO la pAloma", es_palindromo("amO la pAloma"))
print("abba", es_palindromo("abba"))
print("hola mundo", es_palindromo("hola mundo"))
print("rEconocer", es_palindromo("rEconocer"))
