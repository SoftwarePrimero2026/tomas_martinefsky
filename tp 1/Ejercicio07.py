Edad = input("Ingrese su edad: ")
if int(Edad) > 60:
    print("Usted es un adulto mayor")
elif int(Edad) < 18:
    print("Usted es menor de edad")
elif int(Edad) >= 18 and int(Edad) <= 60:
    print("Usted es mayor de edad")