import numpy as np

# Definir los conjuntos de datos
datos1 = np.array([1, 2, 3, 4, 5])
datos2 = np.array([6, 7, 8, 9, 10])

# Calcular la media
media1 = np.mean(datos1)
media2 = np.mean(datos2)

# Calcular la desviación estándar
desviacion1 = np.std(datos1)
desviacion2 = np.std(datos2)

print(f"Media del conjunto de datos 1: {media1}")
print(f"Desviación estándar del conjunto de datos 1: {desviacion1}")
print(f"Media del conjunto de datos 2: {media2}")
print(f"Desviación estándar del conjunto de datos 2: {desviacion2}")