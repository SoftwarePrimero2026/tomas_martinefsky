datos = {"nombre": "Carlos", "edad": None, "ciudad": "Madrid", "telefono": None}

diccionario_limpio = {clave: valor for clave, valor in datos.items() if valor is not None}
print(diccionario_limpio)