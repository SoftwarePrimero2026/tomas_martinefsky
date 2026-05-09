nota = float(input("Ingrese la nota del alumno (0 a 10): "))

if nota >= 9:
    print("Condición: Excelente")
elif nota >= 7:
    print("Condición: Muy bien")
elif nota >= 6:
    print("Condición: Bien")
elif nota >= 4:
    print("Condición: Regular")
else:
    print("Condición: Insuficiente")