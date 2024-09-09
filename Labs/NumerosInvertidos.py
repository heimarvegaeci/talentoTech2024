def invertir_numero(numero):
    numero_invertido = 0
    while numero > 0:
        digito = numero % 10
        numero_invertido = numero_invertido * 10 + digito
        numero = numero // 10
    return numero_invertido

# Solicitar al usuario que ingrese un número entero
numero = int(input("Introduce un número entero: "))
print("Número invertido:", invertir_numero(numero))