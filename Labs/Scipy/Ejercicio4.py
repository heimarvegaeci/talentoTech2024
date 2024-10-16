# Solución Ejercicio 4
from scipy.stats import norm

# Calculamos la probabilidad acumulada (CDF) para el valor 1.96
prob = norm.cdf(1.96, loc=0, scale=1)
print(f"Probabilidad acumulada: {prob}")