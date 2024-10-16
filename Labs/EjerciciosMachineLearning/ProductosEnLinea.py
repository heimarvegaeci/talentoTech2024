import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generar datos aleatorios
np.random.seed(42)
num_samples = 100

data = {
    'Cliente_ID': np.arange(1, num_samples + 1),
    'Edad': np.random.randint(18, 70, size=num_samples),
    'Genero': np.random.randint(0, 2, size=num_samples),
    'Tiempo_En_Linea': np.random.randint(1, 120, size=num_samples),
    'Paginas_Visitadas': np.random.randint(1, 20, size=num_samples),
    'Compra': np.random.randint(0, 2, size=num_samples)
}

df = pd.DataFrame(data)

# Guardar en un archivo CSV
df.to_csv('compras_online.csv', index=False)

# Cargar los datos
df = pd.read_csv('compras_online.csv')

# Separar características y etiquetas
X = df[['Edad', 'Genero', 'Tiempo_En_Linea', 'Paginas_Visitadas']]
y = df['Compra']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo SVM
model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')