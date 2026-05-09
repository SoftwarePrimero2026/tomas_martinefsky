lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

# Convertir a conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Operaciones
interseccion = conjunto1 & conjunto2
union = conjunto1 | conjunto2

print("Elementos comunes:", interseccion)
print("Unión:", union) 