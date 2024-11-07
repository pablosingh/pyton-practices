# Coleccion con llave y valor
# primer elemento String y el otro cualquiera siempre

diccio = {"llave": 10, "otra": 50}
punto = {"x": 1, "y": 5}

print(diccio)
print(punto)

punto["z"] = 45
print(punto)

if "cualquiera" in punto:
    print("Si se encuentra")
else:
    print("No se encuentra")

print(punto.get("llave"))
print(punto.get("llave", 100))
del punto["x"]
del (punto["y"])
print(punto)
