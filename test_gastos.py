import pytest
from gastos import calcular_promedio_gastos, registrar_gasto, calcular_total_gastos
# Probar que se pueda registrar correctamente un gasto con datos válidos, alimentacion, iess,
# ayuda a familia.
def test_registrar_gasto_valido():
    gasto = registrar_gasto("2026-10-01", 50.0, "Alimentación", "Compras de comida")
    assert gasto["fecha"] == "2026-10-01"
    assert gasto["monto"] == 50.0
    assert gasto["categoria"] == "Alimentación"
    assert gasto["descripcion"] == "Compras de comida"  
# Probar que se rechace un gasto cuando el monto sea cero o negativo.
def test_registrar_gasto_monto_invalido():
    with pytest.raises(ValueError):
        registrar_gasto("2026-10-01", 0, "Alimentación", "Compras de comida")
    with pytest.raises(ValueError):
        registrar_gasto("2026-10-01", -10, "Alimentación", "Compras de comida")
# Probar que se rechace un gasto cuando la categoría no esté permitida.
def test_registrar_gasto_categoria_invalida():
    with pytest.raises(ValueError):
        registrar_gasto("2026-10-01", 50.0, "Categoría inválida", "Compras de comida")  
# Probar que se calcule correctamente el total de una lista de gastos.
def test_calcular_total_gastos():
    gasto1 = registrar_gasto("2026-10-01", 50.0, "Alimentación", "Compras de comida")
    gasto2 = registrar_gasto("2026-10-02", 100.0, "Transporte", "Gasolina")
    gasto3 = registrar_gasto("2026-10-03", 200.0, "Vivienda", "Alquiler")
    lista_gastos = [gasto1, gasto2, gasto3]
    total = calcular_total_gastos(lista_gastos)
    assert total == 350.0
# Probar que se calcule correctamente el promedio de una lista de gastos.
def test_calcular_promedio_gastos():
    gasto1 = registrar_gasto("2026-10-01", 50.0, "Alimentación", "Compras de comida")
    gasto2 = registrar_gasto("2026-10-02", 100.0, "Transporte", "Gasolina")
    gasto3 = registrar_gasto("2026-10-03", 200.0, "Vivienda", "Alquiler")
    lista_gastos = [gasto1, gasto2, gasto3]
    promedio = calcular_promedio_gastos(lista_gastos)
    assert promedio == 116.66666666666667
# Probar el flujo completo de registrar gastos y obtener el total y el promedio.
def test_flujo_completo_gastos():
    gasto1 = registrar_gasto("2026-10-01", 50.0, "Alimentación", "Compras de comida")
    gasto2 = registrar_gasto("2026-10-02", 100.0, "Transporte", "Gasolina")
    gasto3 = registrar_gasto("2026-10-03", 200.0, "Vivienda", "Alquiler")
    lista_gastos = [gasto1, gasto2, gasto3]
    total = calcular_total_gastos(lista_gastos)
    promedio = calcular_promedio_gastos(lista_gastos)
    assert total == 350.0
    assert promedio == 116.66666666666667
    