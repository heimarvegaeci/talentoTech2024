import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Generar datos aleatorios
np.random.seed(42)
num_estudiantes = 100

data = {
    'Estudiante_ID': np.arange(1, num_estudiantes + 1),
    'Edad': np.random.randint(15, 41, num_estudiantes),
    'Ingreso_Familiar': np.random.randint(1000, 5001, num_estudiantes),
    'Materias_Inscritas': np.random.randint(1, 8, num_estudiantes),
    'Calificacion_Promedio': np.random.uniform(0, 100, num_estudiantes)
}

df = pd.DataFrame(data)

# Asignar la columna Desercion
df['Desercion'] = df.apply(lambda row: 1 if row['Edad'] < 22 and row['Ingreso_Familiar'] < 1500 and row['Calificacion_Promedio'] < 65 else 0, axis=1)

# Guardar el conjunto de datos en un archivo CSV
df.to_csv('desercion_estudiantil.csv', index=False)

# Cargar el conjunto de datos
df = pd.read_csv('desercion_estudiantil.csv')

# Separar características y etiquetas
X = df[['Edad', 'Ingreso_Familiar', 'Materias_Inscritas', 'Calificacion_Promedio']]
y = df['Desercion']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo SVM
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Realizar predicciones
y_pred = svm_model.predict(X_test)

# Evaluar el modelo
print(classification_report(y_test, y_pred))
# Realizar predicciones para nuevos datos
nuevos_datos = pd.DataFrame({
    'Edad': [20, 25, 30],
    'Ingreso_Familiar': [1200, 3000, 4500],
    'Materias_Inscritas': [3, 5, 6],
    'Calificacion_Promedio': [60, 80, 90]
})

predicciones_nuevas = svm_model.predict(nuevos_datos)
print("Predicciones para nuevos datos:", predicciones_nuevas)