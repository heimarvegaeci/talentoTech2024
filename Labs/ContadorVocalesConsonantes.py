def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    conteo_vocales = 0
    conteo_consonantes = 0

    for char in cadena:
        if char.isalpha():
            if char in vocales:
                conteo_vocales += 1
            else:
                conteo_consonantes += 1

    return conteo_vocales, conteo_consonantes

def main():
    cadena = input("Introduce una cadena de texto: ")
    vocales, consonantes = contar_vocales_consonantes(cadena)
    print(f"Vocales: {vocales}")
    print(f"Consonantes: {consonantes}")

if __name__ == "__main__":
    main()