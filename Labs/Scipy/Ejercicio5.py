# Solución Ejercicio 5
from scipy.spatial import distance

# Definimos los puntos
p1 = [1, 2]
p2 = [4, 6]

# Calculamos la distancia euclidiana
dist = distance.euclidean(p1, p2)
print(f"Distancia euclidiana: {dist}")