for i in range(2):
    edad = int(input("Introduce tu edad: "))
    if edad > 18:
        print("Sin descuento")
    elif edad == 18:
        print("50% de descuento")
    else:
        print("10% de descuento")
print("Fin del programa")