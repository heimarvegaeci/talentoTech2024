def convertir_bases(numero_decimal):
    binario = bin(numero_decimal)
    octal = oct(numero_decimal)
    hexadecimal = hex(numero_decimal)
    
    return binario, octal, hexadecimal

def main():
    try:
        numero_decimal = int(input("Introduce un número decimal: "))
        binario, octal, hexadecimal = convertir_bases(numero_decimal)
        
        print(f"Binario: {binario}")
        print(f"Octal: {octal}")
        print(f"Hexadecimal: {hexadecimal}")
    except ValueError:
        print("Por favor, introduce un número decimal válido.")

if __name__ == "__main__":
    main()