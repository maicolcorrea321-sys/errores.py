# ============================================================
# OPERADORES ARITMÉTICOS EN PYTHON
# ============================================================
numero1 = float(print("ingrese el número 1: "))
numero2 = float(print("ingrese el número 2: "))

suma           = numero1 + numero2   
resta          = numero1 - numero2   
multiplicacion = numero1 * numero2   
division       = numero1 / numero2   
division_entera= numero1 // numero2  
residuo        = numero1 % numero2   
potencia       = numero1 ** numero2  

print(f"""
Resultado de Operaciones Aritméticas:
suma:            {numero1} +  {numero2} = {suma}
resta:           {numero1} -  {numero2} = {resta}
multiplicacion:  {numero1} *  {numero2} = {multiplicacion}
division:        {numero1} /  {numero2} = {division:.4f}
division_entera: {numero1} // {numero2} = {division_entera}
residuo:         {numero1} %  {numero2} = {residuo}
potencia:        {numero1} ** {numero2} = {potencia}
""")