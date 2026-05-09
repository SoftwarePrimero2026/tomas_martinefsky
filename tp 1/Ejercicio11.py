Edad = input("Ingrese su edad: ")
Carnet = input("¿Posee carnet de estudiante? (si/no): ")                    

if int(Edad) >= 18 and Carnet.lower() == "si":
    print("Usted puede acceder al descuento.")
else:
    print("Usted no puede acceder al descuento.")