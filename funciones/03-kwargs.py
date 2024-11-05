def get_product(**datos):
    print(datos)
    print(datos["name"])


get_product(name="pc",
            desc="descripcion",
            price=199.99)
