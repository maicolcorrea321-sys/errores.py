"""
try:
    numero = int(input("Ingrese un número:"))
    print(f"El numero ingresado: {numero}")
except ValueError:
    print("ingrese un número valido")
"""
menu = 0

while menu != 3:
    try: 

        menu = int(input("""
        seleccione una opcion:
        1. sumar
        2. restar
        3. salir
        : """))

        if menu == 1:
            n1 = int(input("Ingrese primer número: "))
            n2 = int(input("Ingrese segundo número: "))
            print(f"Resultado {n1+n2}")

        elif menu == 2:
                n1 = int(input("Ingrese primer número:"))
                n2 = int(input("Ingrese segundo número: "))
                print(f"Resultado {n1-n2}")
        else:
            print("Opción Invalida")
    except ValueError:
        print("Inserte un numero valido")
        

print("fuera del sistema")