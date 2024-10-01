import numpy as np


def producto_matrices(matriz1, matriz2):
    if matriz1.shape != matriz2.shape:
        print("Las matrices deben ser cuadradas y del mismo tamaño")        
    return np.dot(matriz1, matriz2)

# Ejemplo de uso
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = producto_matrices(matriz1, matriz2)
print(resultado)