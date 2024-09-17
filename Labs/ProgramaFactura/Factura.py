class Factura:
    def __init__(self, precio_unitario, porcentaje_iva, cantidad):
        self.precio_unitario = precio_unitario
        self.porcentaje_iva = porcentaje_iva
        self.cantidad = cantidad

    def calcular_factura(self):
        subtotal_sin_iva = self.precio_unitario / (1 + (self.porcentaje_iva / 100)) * self.cantidad
        descuentos = self.descuento_factura(subtotal_sin_iva)
        valor_iva = subtotal_sin_iva * (self.porcentaje_iva / 100)
        total_con_iva = subtotal_sin_iva - descuentos + valor_iva 
        return subtotal_sin_iva, descuentos, valor_iva, total_con_iva

    def descuento_factura(self, subtotal_sin_iva):
        if 500000 <= subtotal_sin_iva <= 999999:
            descuento = subtotal_sin_iva * 0.10
        elif 1000000 <= subtotal_sin_iva <= 1999999:
            descuento = subtotal_sin_iva * 0.20
        elif subtotal_sin_iva >= 2000000:
            descuento = subtotal_sin_iva * 0.30
        else:
            descuento = 0
        return descuento
    
    # def cacular_total_con_descuento(self, cantidad, subtotal_sin_iva, valor_iva, descuento):
    #     subtotal_con_descuento = (subtotal_sin_iva - descuento)*cantidad
    #     total_con_iva = subtotal_con_descuento + valor_iva* cantidad
    #     return total_con_iva,subtotal_con_descuento
