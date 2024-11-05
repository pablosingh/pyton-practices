# for j in range(3):
#     for k in range(3):
#         print(f"{j} , {k}")

comando = ""
numero = float(input("1er numero : "))
while True:
    comando = input("Comando : ")
    if comando.lower() == "salir":
        break
    numero_dos = float(input("2do numero : "))
    if comando.lower() == "suma":
        numero += numero_dos
    elif comando.lower() == "resta":
        numero -= numero_dos
    elif comando.lower() == "multi":
        numero *= numero_dos
    elif comando.lower() == "divi":
        numero /= numero_dos
    else:
        print("comando invalido")
        break
    print(f"Resultado : {numero}")
