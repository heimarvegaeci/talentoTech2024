import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Reshape para sklearn
x = x.reshape(-1, 1)

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(x, y)

# Calcular pendiente e intercepto
slope = model.coef_[0]
intercept = model.intercept_

# Predecir valores
y_pred = model.predict(x)

# Calcular el error cuadrático medio
mse = mean_squared_error(y, y_pred)

# Imprimir resultados
print(f'Pendiente: {slope}')
print(f'Intercepto: {intercept}')
print(f'Error Cuadrático Medio: {mse}')

# Graficar los datos y la regresión
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, y_pred, color='red', label='Regresión Lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal')
plt.legend()
plt.show()