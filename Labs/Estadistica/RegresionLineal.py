import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Predecir valores
X_new = np.array([[0], [2]])
y_predict = model.predict(X_new)

# Graficar los datos y la línea de regresión
plt.scatter(X, y, color='blue', label='Datos')
plt.plot(X_new, y_predict, color='red', label='Línea de regresión')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.legend()
plt.show()