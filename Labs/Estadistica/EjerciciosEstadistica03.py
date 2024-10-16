import numpy as np
from scipy.stats import pearsonr

import matplotlib.pyplot as plt

# Datos de ejemplo
x = np.array([10, 20, 30, 40, 50])
y = np.array([15, 25, 35, 45, 55])

# Calcular la correlación de Pearson
correlation, _ = pearsonr(x, y)
print(f'Correlación de Pearson: {correlation}')

# Graficar los datos y la línea de tendencia
plt.scatter(x, y, label='Datos')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='red', label='Línea de tendencia')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de correlación entre X y Y')
plt.legend()
plt.show()