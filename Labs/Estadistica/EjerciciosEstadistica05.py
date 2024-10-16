import numpy as np

import matplotlib.pyplot as plt

# Conjuntos de datos
datos1 = [1, 2, 3, 4, 5]
datos2 = [1, 2, 3, 4, 5]

# Calcular media y desviación estándar
media1 = np.mean(datos1)
desviacion_estandar1 = np.std(datos1)

media2 = np.mean(datos2)
desviacion_estandar2 = np.std(datos2)

print(f"Conjunto de datos 1: Media = {media1}, Desviación Estándar = {desviacion_estandar1}")
print(f"Conjunto de datos 2: Media = {media2}, Desviación Estándar = {desviacion_estandar2}")

# Graficar los datos
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(datos1, bins=5, alpha=0.7, color='blue', label='Datos 1')
plt.axvline(media1, color='red', linestyle='dashed', linewidth=1)
plt.title('Histograma de Datos 1')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(datos2, bins=5, alpha=0.7, color='green', label='Datos 2')
plt.axvline(media2, color='red', linestyle='dashed', linewidth=1)
plt.title('Histograma de Datos 2')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()

plt.tight_layout()
plt.show()