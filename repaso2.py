"""
#variables
#condicionales
#ciclos
#manejo de errores.

#Empresa de bus que vende tiquetes desde Medellín:


Medellín -> Bogotá= 120000
Medellín -> Cali = 100000
Medellín -> Barranquilla= 150000
Medellín -> Cartagena = 200000

Proceso de compra:
Solicitar:
Destino, 
Cantidad de tiquetes
Segun la cantidad de tiquetes pedir los nombres de los pasajeros. 
Calcular total a pagar.
Mostrar destino, los nombres de los pasajeros, total a pagar.

"""
#ciclo infinito

while True:
    print("===Tiquete de bus===\n")

    try:
        menu=int(input("""
        seleccione  la ruta a comprar
        1. Medellín - Bogotá
        2. Medellín - Cali
        3. Medellín - Barranquilla
        4. Medellín - Cartagena
        5. Salir:  """))

        #condicional: verifica la opción escogida
        if menu in range(1,5):
            valor_tiquete=0
            if menu ==1:
                valor_tiquete=120000
                Ruta= "Medellín - Bogotá"
            elif menu ==2:
                valor_tiquete=100000
                Ruta = "Medellín - Cali"
            elif menu ==3:
                valor_tiquete=150000
                Ruta = "Medellín - Barranquilla" 
            else: 
                valor_tiquete =200000
                Ruta = "Medellín - Cartagena"


            try:
                cantidad = int(input("Cantidad de tiqutes a comprar: "))
                lista_pasajero =[] 
                for i in range(cantidad):
                    pasajero=input(f"Ingrese el nombre del pasajero:  {i+1}")
                    #Guardar el valor de la variable en la lista
                    lista_pasajero.append(pasajero)

                #mostrar todo
                print(f"""
                === Resumen compra ===
                - Ruta = {Ruta}
                - Cantidad de pasajeros= {cantidad}
                - Valor tiquete = {valor_tiquete}
                - Total : {cantidad * valor_tiquete}
                - Pasajero = {lista_pasajero}
                """)
                
            except ValueError:
                print("Ingrese una cantidad valida")


        elif menu ==5:
            print("Saliendo del sistema")
            break
        else:
            print("Opción Invalida")
            break

    except ValueError:
        print("ingrese una opción valida.")


    
