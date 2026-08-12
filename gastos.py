# Crear una función para registrar un gasto con fecha, monto, categoría y descripción.
def registrar_gasto(fecha, monto, categoria, descripcion):
#Registra un gasto personal
# Validar que el monto sea mayor que cero y devolver los datos del gasto registrados.
    if monto <=  0:
        raise ValueError("El monto del gasto debe ser mayor que cero.")
# Validar que la categoría sea una de las categorías permitidas.
    categorias_permitidas = [ "Alimentación", "Ayuda familiar", "Educación", "Entretenimiento",  "IESS",
    "Otros", "Salud","Servicios", "Transporte","Vivienda"]
    if categoria not in categorias_permitidas:
        raise ValueError(f"La categoría '{categoria}' no es válida. Debe ser una de: {', '.join(categorias_permitidas)}.")
# Crear y devolver el gasto registrado con sus datos.
    gasto = {
        "fecha": fecha,
        "monto": monto,
        "categoria": categoria,
        "descripcion": descripcion
    }
    return gasto    
# Crear una función que calcule el total de los montos de una lista de gastos.
def calcular_total_gastos(lista_gastos):
#Calcula el total de gastos
    total = 0
    for gasto in lista_gastos:
        total += gasto["monto"]
    return total
# Crear una función que calcule el promedio de los montos de una lista de gastos.
def calcular_promedio_gastos(lista_gastos):
#Calcula el promedio de gastos
    if not lista_gastos:
        return 0
    total = calcular_total_gastos(lista_gastos)
    promedio = total / len(lista_gastos)
    return promedio

