def calcular_cantidad_carne(numGallinas, numGallos, numPollitos):
    peso_gallina = 6
    peso_gallo = 7
    peso_pollito = 1
    
    total_carne = (numGallinas * peso_gallina) + (numGallos * peso_gallo) + (numPollitos * peso_pollito)
    return total_carne

# Ejemplo de uso
N = 10  # Número de gallinas
M = 5   # Número de gallos
K = 20  # Número de pollitos

print(f"Cantidad total de carne: {calcular_cantidad_carne(10, 5, 20)} kilos")
