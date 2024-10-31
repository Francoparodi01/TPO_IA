# Función para ingresar datos de empleados por el usuario
def ingresar_empleados():
    empleados = []
    print("Ingrese los datos de los empleados. Escriba 'fin' para terminar.")
    
    while True:
        nombre = input("Nombre del empleado (o 'fin' para salir): ")
        if nombre.lower() == 'fin':
            break
        categoria = input("Categoría (Junior, SemiSenior, Senior): ")
        sueldo = float(input("Sueldo: "))
        antiguedad = int(input("Antigüedad en años: "))
        rotacion = input("¿Ha rotado? (si/no): ").lower() == 'si'
        desempeno = int(input("Desempeño (escala 1-10): "))
        
        # Agregar empleado a la lista
        empleados.append([nombre, categoria, sueldo, antiguedad, rotacion, desempeno])
        print(f"Empleado {nombre} agregado.\n")

    return empleados

# Función para analizar la promoción (antigüedad + desempeño)
def analisis_promocion(empleados, min_antiguedad, min_desempeno):
    promocionables = []
    for empleado in empleados:
        if empleado[3] >= min_antiguedad and empleado[5] >= min_desempeno:
            promocionables.append(empleado[0])  # Solo se añade el nombre del empleado
    return promocionables

# Función para análisis del desempeño
def analisis_desempeno(empleados):
    desempenos = [empleado[5] for empleado in empleados]
    promedio_desempeno = sum(desempenos) / len(desempenos) if desempenos else 0
    bajo_desempeno = [empleado[0] for empleado in empleados if empleado[5] < 6]
    
    return promedio_desempeno, bajo_desempeno

# Función para calcular la eficiencia en % según desempeño
def eficiencia_tareas(empleado):
    return empleado[5] * 10  # Si el desempeño es 8, la eficiencia será 80%

# Función para analizar los posibles despidos
def analisis_despido(empleados, min_desempeno):
    posibles_despidos = []
    for empleado in empleados:
        if empleado[4] or empleado[5] < min_desempeno:
            posibles_despidos.append(empleado[0])
    return posibles_despidos

# Función principal para ejecutar el análisis automáticamente tras ingresar empleados
def ejecutar_analisis():
    # Ingresar empleados
    empleados = ingresar_empleados()

    # Mostrar el análisis
    print("\nAnálisis de Promoción:")
    promocionables = analisis_promocion(empleados, min_antiguedad=3, min_desempeno=7)
    if promocionables:
        print(f"Empleados con posibilidad de promoción: {promocionables}")
    else:
        print("No hay empleados elegibles para promoción.")

    print("\nAnálisis de Desempeño:")
    promedio, bajos = analisis_desempeno(empleados)
    print(f"Promedio de desempeño: {promedio}")
    print(f"Empleados con bajo desempeño: {bajos}")

    print("\nEficiencia en las tareas (%):")
    for empleado in empleados:
        print(f"Eficiencia de {empleado[0]}: {eficiencia_tareas(empleado)}%")

    print("\nAnálisis de Despido:")
    despidos = analisis_despido(empleados, min_desempeno=5)
    if despidos:
        print(f"Empleados en riesgo de despido: {despidos}")
    else:
        print("No hay empleados en riesgo de despido.")

# Ejecutar el análisis tras ingresar los empleados
ejecutar_analisis()
