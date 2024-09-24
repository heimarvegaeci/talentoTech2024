# Importar la librería NumPy
import numpy as np

# Crear dos matrices
matriz_a = np.array([[1, 2, 3], [4, 5, 6]])
matriz_b = np.array([[7, 8, 9], [10, 11, 12]])

# Realizar una suma de matrices
suma = matriz_a + matriz_b

# Realizar una multiplicación de matrices
producto = np.dot(matriz_a, matriz_b.T)

# Mostrar los resultados
print("Suma de matrices:\n", suma)
print("\nProducto de matrices:\n", producto)