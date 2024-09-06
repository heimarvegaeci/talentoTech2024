def calcular_factura():
    precio_unitario = float(input("Ingrese el precio unitario con IVA incluido: "))
    porcentaje_iva = float(input("Ingrese el porcentaje del IVA: "))
    cantidad = int(input("Ingrese la cantidad que se va a comprar: "))

    subtotal_sin_iva = precio_unitario / (1 + (porcentaje_iva / 100))
    valor_iva = subtotal_sin_iva * (porcentaje_iva / 100)
    total_con_iva = precio_unitario * cantidad

    print(f"Subtotal sin IVA: {subtotal_sin_iva:.2f}")
    print(f"Valor del IVA:{valor_iva:.2f} , Porcentaje:{porcentaje_iva:.2f}%")
    print(f"Total con IVA: {total_con_iva:.2f}")

calcular_factura()