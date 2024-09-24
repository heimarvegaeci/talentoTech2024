# Labs/ProgramaNomina/test_calculos_nomina.py

import pytest
from .Empleado import Empleado
from .CalculosNomina import CalculosNomina

@pytest.fixture
def empleado():
    return Empleado(54987654, "Catalina Hernandez", 6000000, 22, 10, 5, 2, 20, 18)

@pytest.fixture
def calculos_nomina(empleado: Empleado):
    return CalculosNomina(empleado)

def test_calcular_salario(calculos_nomina: CalculosNomina):
    salario_devengado = calculos_nomina.calcular_salario()
    assert pytest.approx(salario_devengado, 0.01) == 2000000