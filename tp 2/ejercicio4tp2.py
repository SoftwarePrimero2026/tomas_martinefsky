contactos = {
    "Ana": "123456789",
    "Luis": "987654321",
    "Carlos": "456789123"
}

# Búsqueda
nombre_buscar = input("Ingrese el nombre del contacto: ")
telefono = contactos.get(nombre_buscar, "Contacto no encontrado")
print(f"Teléfono: {telefono}")