import pytest
from .Factura import Factura

@pytest.fixture
def facturaSinDescuento():
    return Factura(50000, 19, 10)  # Ejemplo: precio_unitario=500000, porcentaje_iva=20, cantidad=10

def test_calcular_factura_sin_descuento(facturaSinDescuento):
  
    valor_descuento_esp = 0
    valor_iva_esp = 79831.93
    subtotal_sin_iva_esp = 420168.67
    total_con_iva_esp = 500000
    
    subtotal_sin_iva, valor_descuento, valor_iva, total_con_iva = facturaSinDescuento.calcular_factura()

    assert pytest.approx(subtotal_sin_iva_esp, 0.01) == subtotal_sin_iva
    assert pytest.approx(valor_descuento_esp, 0.01) == valor_descuento
    assert pytest.approx(valor_iva_esp, 0.01) == valor_iva
    assert pytest.approx(total_con_iva_esp, 0.01) == total_con_iva

def test_calcular_facturaDescuento10():
    
    factura = Factura(70000,19,10)

    valor_descuento_esp = 58823.53
    valor_iva_esp = 111764.71
    subtotal_sin_iva_esp = 588235.29
    total_con_iva_esp = 641176.47
    
    subtotal_sin_iva, valor_descuento, valor_iva, total_con_iva = factura.calcular_factura()

    assert pytest.approx(subtotal_sin_iva_esp, 0.01) == subtotal_sin_iva
    assert pytest.approx(valor_descuento_esp, 0.01) == valor_descuento
    assert pytest.approx(valor_iva_esp, 0.01) == valor_iva
    assert pytest.approx(total_con_iva_esp, 0.01) == total_con_iva

def test_calcular_facturaDescuento20():
    
    factura = Factura(200000,19,10)

    valor_descuento_esp = 336134.45
    valor_iva_esp = 319327.73
    subtotal_sin_iva_esp = 1680672.27
    total_con_iva_esp = 1663865.55
    
    subtotal_sin_iva, valor_descuento, valor_iva, total_con_iva = factura.calcular_factura()

    assert pytest.approx(subtotal_sin_iva_esp, 0.01) == subtotal_sin_iva
    assert pytest.approx(valor_descuento_esp, 0.01) == valor_descuento
    assert pytest.approx(valor_iva_esp, 0.01) == valor_iva
    assert pytest.approx(total_con_iva_esp, 0.01) == total_con_iva

def test_calcular_facturaDescuento30():
    
    factura = Factura(500000,19,10)

    valor_descuento_esp = 1260504.20
    valor_iva_esp = 798319.33
    subtotal_sin_iva_esp = 4201680.67
    total_con_iva_esp = 3739495.80
    
    subtotal_sin_iva, valor_descuento, valor_iva, total_con_iva = factura.calcular_factura()

    assert pytest.approx(subtotal_sin_iva_esp, 0.01) == subtotal_sin_iva
    assert pytest.approx(valor_descuento_esp, 0.01) == valor_descuento
    assert pytest.approx(valor_iva_esp, 0.01) == valor_iva
    assert pytest.approx(total_con_iva_esp, 0.01) == total_con_iva