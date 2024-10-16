import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(0)
empleado_id = np.arange(1, 101)
años_experiencia = np.random.randint(1, 21, size=100)
salario = años_experiencia * 5000 + np.random.normal(0, 10000, size=100)

# Crear DataFrame
data = pd.DataFrame({
    'Empleado_ID': empleado_id,
    'Años_Experiencia': años_experiencia,
    'Salario': salario
})

# Guardar en un archivo CSV
data.to_csv('salarios_experiencia.csv', index=False)

# Cargar los datos
data = pd.read_csv('salarios_experiencia.csv')

# Separar las características y la variable objetivo
X = data[['Años_Experiencia']]
y = data['Salario']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Crear el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predecir los salarios en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Visualizar los resultados
plt.scatter(X_test, y_test, color='red', label='Datos Reales')
plt.plot(X_test, y_pred, color='blue', label='Predicciones')
plt.title('Salario vs Años de Experiencia')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.legend()
plt.show()

# Predecir el salario de un empleado con un número específico de años de experiencia
años_experiencia_nuevo = np.array([[10]])
salario_predicho = modelo.predict(años_experiencia_nuevo)
print(f'El salario predicho para 10 años de experiencia es: {salario_predicho[0]:.2f}')