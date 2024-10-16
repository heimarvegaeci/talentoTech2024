import numpy as np

import matplotlib.pyplot as plt

# Datos de ejemplo
datos = np.array([10, 20, 30, 40, 50])

# Calcular la media
media = np.mean(datos)

# Graficar los datos y la media
plt.plot(datos, 'bo-', label='Datos')
plt.axhline(y=media, color='r', linestyle='--', label=f'Media: {media:.2f}')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Datos y su Media')
plt.legend()
plt.show()
