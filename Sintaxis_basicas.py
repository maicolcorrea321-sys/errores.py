# ============================================================
# INTRODUCCIÓN A LAS VARIABLES EN PYTHON
# ============================================================

# Una variable permite almacenar un dato para utilizarlo
# posteriormente dentro del programa.

nombre       = "Eli"       # Variable de tipo string (cadena de texto)
documento    = 123         # Variable de tipo int (número entero)
direccion    = "Medellín"  # Variable de tipo string (cadena de texto)
tiene_deudas = True        # Variable de tipo bool (booleano)


# ============================================================
# MOSTRAR EL CONTENIDO DE UNA VARIABLE
# ============================================================
print(nombre)

# ============================================================
# CONCATENACIÓN USANDO +
# ============================================================
print("CONCATENACIÓN USANDO +")
print("=" * 30)

# El operador + permite unir textos.
# Cuando usamos +, todos los elementos deben ser strings.
#
# documento es un entero (int), por lo que esta línea
# produciría un error:
#
# print("Mi nombre es: " + nombre + " y mi documento es: " + documento)

# Para solucionarlo, podemos convertir el número a texto
# utilizando str().
print("Mi nombre es: " + nombre + " y mi documento es: " + str(documento))


# ============================================================
# CONCATENACIÓN USANDO ,
# ============================================================
print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)

# Al utilizar comas, Python permite mostrar diferentes
# tipos de datos sin necesidad de convertirlos a string.
print("Mi nombre es:", nombre, "y mi documento es:", documento)


# ============================================================
# CONCATENACIÓN USANDO F-STRINGS
# ============================================================
print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

# Las f-strings permiten insertar variables directamente
# dentro de un texto.
#
# Se coloca la letra f antes de las comillas y las variables
# se escriben entre llaves { }.
print(f"Mi nombre es: {nombre} y mi documento es: {documento}")


# ============================================================
# F-STRINGS CON VARIAS VARIABLES
# ============================================================
print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

# Las f-strings también permiten crear textos
# de varias líneas utilizando triple comilla.
print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")


# ============================================================
# F-STRINGS CON COMILLAS SIMPLES
# ============================================================

# También podemos utilizar tres comillas simples (''')
# para crear textos de varias líneas.
print("=" * 30)

print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deudas}
""")


# SALTO DE LÍNEA EN PYTHON

# \n representa un salto de línea.
# Salto de línea al inicio del texto
print(f"\n Hola, {nombre}!")

# Salto de línea al final del texto
print(f"Bienvenida {nombre} a Python.\n")