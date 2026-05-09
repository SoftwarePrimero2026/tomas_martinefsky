# Lista original
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]

# Convertir a conjunto para eliminar duplicados
conjunto_unico = set(lista_con_duplicados)

# Volver a lista
lista_sin_duplicados = list(conjunto_unico)

print(lista_sin_duplicados)