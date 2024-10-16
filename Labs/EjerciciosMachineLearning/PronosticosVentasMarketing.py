import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generar datos aleatorios
np.random.seed(42)
n = 500
data = {
    'Campaña_ID': np.arange(1, n + 1),
    'Publicidad_TV': np.random.uniform(1000, 50000, n),
    'Publicidad_Radio': np.random.uniform(1000, 30000, n),
    'Publicidad_Redes_Sociales': np.random.uniform(1000, 20000, n),
    'Ventas': np.random.uniform(1000, 100000, n)
}

df = pd.DataFrame(data)

# Guardar el conjunto de datos en un archivo CSV
df.to_csv('ventas_marketing.csv', index=False)

# Cargar el conjunto de datos
df = pd.read_csv('ventas_marketing.csv')

# Definir las variables independientes (X) y la variable dependiente (y)
X = df[['Publicidad_TV', 'Publicidad_Radio', 'Publicidad_Redes_Sociales']]
y = df['Ventas']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal múltiple
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Error cuadrático medio: {mse}')

# Mostrar los coeficientes del modelo
print('Coeficientes del modelo:')
print(f'Intercepto: {model.intercept_}')
print(f'Publicidad_TV: {model.coef_[0]}')
print(f'Publicidad_Radio: {model.coef_[1]}')
print(f'Publicidad_Redes_Sociales: {model.coef_[2]}')