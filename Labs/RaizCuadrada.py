def calcular_raiz_cuadrada(numero):
    if numero < 0:
        return "Un número negativo no tiene raíz cuadrada real."
    
    aproximacion = numero / 2.0
    tolerancia = 0.000001
    while True:
        mejor_aproximacion = (aproximacion + numero / aproximacion) / 2.0
        if abs(aproximacion - mejor_aproximacion) < tolerancia:
            return mejor_aproximacion
        aproximacion = mejor_aproximacion

numero = float(input("Ingrese un número: "))
resultado = calcular_raiz_cuadrada(numero)
print(f"La raíz cuadrada de {numero} es: {resultado}")