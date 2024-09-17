# Main.py
from Factura import Factura

def main():   
    precio_unitario = float(input("Ingrese el precio unitario con IVA incluido: "))
    porcentaje_iva = float(input("Ingrese el porcentaje del IVA: "))
    cantidad = int(input("Ingrese la cantidad que se va a comprar: "))

    factura = Factura(precio_unitario, porcentaje_iva, cantidad)

    subtotal_sin_iva,valor_descuento, valor_iva, total_con_iva = factura.calcular_factura()
    
    
    print(f"Subtotal sin IVA: {subtotal_sin_iva:.2f}")
    print(f"Descuento: {valor_descuento:.2f}")
    print(f"Valor del IVA: {valor_iva:.2f}")
    print(f"Total con IVA: {total_con_iva:.2f}")

if __name__ == "__main__":
    main()