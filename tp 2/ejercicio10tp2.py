frase = "Python es un lenguaje de programación"
vocales = "aeiou"

conjunto_vocales = set(letra.lower() for letra in frase if letra.lower() in vocales)

print(conjunto_vocales)