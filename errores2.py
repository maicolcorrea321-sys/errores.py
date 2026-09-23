# Ejercicio 1 : try / except básico
# Sin manejo de errores, ingresar "hola" en lugar de un número
# provocaría un ValueError y el programa se detendría. 

try:
    numero = int(input("Ingrese un numero: "))
    print: (f"El número ingresado es: {numero}")
except ValueError:
    print("Ingrese un número válido")

# Ejercicio 2: División segura con ZeroDivisionError

try:

    dividendo = float(input("ingrese el dividendo:"))
    divisor = float(input("Ingrese el divisor:"))
    division = dividendo / divisor
    print(f"El resultado es: {division}") 
except ZeroDivisionError:
    print("error: no se puede dividir por cero")
except ValueError:
    print("Ingrese un valor válido")


# Ejercicio 3: else y finally
# else  → se ejecuta solo si NO ocurrió ninguna excepción
# finally → se ejecuta SIEMPRE, con o sin error

try: 
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Debe ser un numero entero")

else: 
    if edad >= 18:
        print("Acceso permitido")
    else: 
        print("Acceso denegado")
finally:
    print("Verificación finalizada")


# Ejercicio 4: Solicitar un dato válido hasta que el usuario lo ingrese correctamente
while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        break   # sale del ciclo si el valor es válido
    except ValueError as e:
        print(f"Entrada inválida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")

# Ejercicio 5: raise — lanzar una excepción personalizada

def calcular_promedio(notas):
    if len(notas)=0:
        raise ValueError("La lista de notas no puede estar vacía.")

try: 
    n = int(input("¿Cuántas notas va a ingresar?"))
    notas = []
    for i in range(n):
        nota = float(input(f" Nota {i+1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error:{e}")