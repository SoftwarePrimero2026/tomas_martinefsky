contador = 0
suma = 0
while True:
    numero = int(input("Ingrese un numero entero (0 para finalizar): "))
    if numero == 0:
        break
    contador += 1
    suma += numero
print(f"Cantidad de numeros ingresados: {contador}")
print(f"Suma total de los numeros ingresados: {suma}")