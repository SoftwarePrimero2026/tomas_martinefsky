productos = []
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    productos.append(producto)
print("\nLista de productos ingresados:")
for index, producto in enumerate(productos, start=1):
    print(f"{index}. {producto}")