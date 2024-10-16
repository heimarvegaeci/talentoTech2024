import numpy as np

import matplotlib.pyplot as plt

# Conjunto de números
datos = np.array([10, 12, 23, 23, 16, 23, 21, 16])

# Cálculo de la media, varianza y desviación estándar
media = np.mean(datos)
varianza = np.var(datos)
desviacion_estandar = np.std(datos)

# Cálculo de la correlación
correlacion = np.corrcoef(datos)
print(f"Correlación: \n{correlacion}")
print(f"Media: {media}")
print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")


# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(datos, 'o', label='Datos')
plt.axhline(y=media, color='r', linestyle='-', label=f'Media: {media:.2f}')
plt.axhline(y=media + desviacion_estandar, color='g', linestyle='--', label=f'Desviación Estándar: {desviacion_estandar:.2f}')
plt.axhline(y=media - desviacion_estandar, color='g', linestyle='--')
plt.title('Datos y su Media, Varianza y Desviación Estándar')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()