import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Reshape de x para que sea una matriz de una sola columna
x = x.reshape(-1, 1)

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(x, y)

# Predicciones
y_pred = model.predict(x)

# Graficar los datos y la línea de regresión
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, y_pred, color='red', label='Línea de regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal')
plt.legend()
plt.show()