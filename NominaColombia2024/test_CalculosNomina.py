import unittest
from Empleado import Empleado
from CalculosNomina import CalculosNomina

class TestCalculosNomina(unittest.TestCase):

    def test_calcular_salario_basico(self):
        empleado = Empleado(12345678, "Juan Perez", 6000000, 22, 10, 5, 2, 20, 18)
        calculos_nomina = CalculosNomina(empleado)
        salario_devengado = calculos_nomina.calcular_salario_basico()
        self.assertAlmostEqual(salario_devengado, 4400000, places=2)  # 6000000 / 30 * 22

    def test_calcular_salud_empleado(self):
        empleado = Empleado(12345678, "Juan Perez", 6000000, 22, 10, 5, 2, 20, 18)
        calculos_nomina = CalculosNomina(empleado)
        deduccion_salud = calculos_nomina.calcular_salud_empleado(6000000)
        self.assertAlmostEqual(deduccion_salud, 240000, places=2)  # 6000000 * 0.04

    def test_calcular_pension_empleado(self):
        empleado = Empleado(12345678, "Juan Perez", 6000000, 22, 10, 5, 2, 20, 18)
        calculos_nomina = CalculosNomina(empleado)
        deduccion_pension = calculos_nomina.calcular_pension_empleado(6000000)
        self.assertAlmostEqual(deduccion_pension, 240000, places=2)  # 6000000 * 0.04

    def test_calcular_auxilio_transporte(self):
        empleado = Empleado(12345678, "Juan Perez", 2000000, 22, 10, 5, 2, 20, 18)
        calculos_nomina = CalculosNomina(empleado)
        auxilio_transporte = calculos_nomina.calcular_auxilio_transporte()
        self.assertAlmostEqual(auxilio_transporte, 118800, places=2)  # Example value, adjust as needed
    
if __name__ == '__main__':
    unittest.main()