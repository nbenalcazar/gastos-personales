# Crear una función para registrar un gasto con fecha, monto, categoría y descripción.
def registrar_gasto(fecha, monto, categoria, descripcion):
# Validar que el monto sea mayor que cero y devolver los datos del gasto registrados.
    if monto <= 0:
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
    total = 0
    for gasto in lista_gastos:
        total += gasto["monto"]
    return total
# Crear una función que calcule el promedio de los montos de una lista de gastos.
def calcular_promedio_gastos(lista_gastos):
    if not lista_gastos:
        return 0
    total = calcular_total_gastos(lista_gastos)
    promedio = total / len(lista_gastos)
    return promedio


   

    # Crear datos de ejemplo con tres gastos y mostrar en pantalla los gastos, el total y el promedio.
gasto1 = registrar_gasto("2026-10-01", 50.0, "Alimentación", "Compras de comida")
gasto2 = registrar_gasto("2026-10-02", 100.0, "Transporte", "Gasolina")
gasto3 = registrar_gasto("2026-10-03", 200.0, "Vivienda", "Alquiler")

lista_gastos = [gasto1, gasto2, gasto3]

print("Gastos registrados:")
for gasto in lista_gastos:
        print(f" - {gasto['fecha']}: {gasto['descripcion']} (${gasto['monto']})")

total = calcular_total_gastos(lista_gastos)
promedio = calcular_promedio_gastos(lista_gastos)

print(f"Total de gastos: ${total}")
print(f"Promedio de gastos: ${promedio}")