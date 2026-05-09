alumnos = []    
while True:
    nombre = input("Ingrese el nombre del alumno (o 'salir' para finalizar): ")
    if nombre.lower() == "salir":
        break
    edad = int(input("Ingrese la edad del alumno: "))
    alumnos.append((nombre, edad))  
print("\nLista de alumnos ingresados:") 
mayores_18 = 0
for alumno in alumnos:
    print(f"Nombre: {alumno[0]}, Edad: {alumno[1]}")
    if alumno[1] >= 18:
        mayores_18 += 1 
print(f"\nCantidad total de alumnos mayores o iguales a 18 años: {mayores_18}")