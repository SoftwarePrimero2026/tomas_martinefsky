diccionario_original = {"a": 1, "b": 2}
diccionario_invertido = {valor: clave for clave, valor in diccionario_original.items()}

print(diccionario_invertido)