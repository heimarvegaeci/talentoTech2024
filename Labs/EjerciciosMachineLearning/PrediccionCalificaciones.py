import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(42)
estudiante_id = np.arange(1, 101)
horas_estudio = np.random.uniform(1, 10, 100)
calificacion_final = 2.5 * horas_estudio + np.random.normal(0, 2, 100)

# Crear DataFrame
data = {
    'Estudiante_ID': estudiante_id,
    'Horas_Estudio': horas_estudio,
    'Calificacion_Final': calificacion_final
}
df = pd.DataFrame(data)

# Guardar en un archivo CSV
df.to_csv('calificaciones_estudio.csv', index=False)

# Cargar los datos
df = pd.read_csv('calificaciones_estudio.csv')

# Preparar los datos para la regresión lineal
X = df[['Horas_Estudio']]
y = df['Calificacion_Final']

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Predecir las calificaciones
y_pred = model.predict(X)

# Visualizar los resultados
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred, color='red', label='Línea de regresión')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación Final')
plt.title('Regresión Lineal Simple')
plt.legend()
plt.show()

# Mostrar coeficientes
print(f'Coeficiente: {model.coef_[0]}')
print(f'Intercepción: {model.intercept_}')