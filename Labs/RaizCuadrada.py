def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    else:
        return numero ** 0.5

# Ejemplo de uso
numero = float(input("Introduce un número: "))
resultado = raiz_cuadrada(numero)
print(f"La raíz cuadrada de {numero} es {resultado}")