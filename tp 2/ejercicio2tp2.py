palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]
frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print(frecuencias)