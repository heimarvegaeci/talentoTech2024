import numpy as np
from scipy.integrate import quad

# Definimos la función f(x) = e^(-x^2)
def f(x):
    return np.exp(-x**2)

# Calculamos la integral de f(x) desde -∞ hasta ∞
resultado, error = quad(f, -np.inf, np.inf)

print(f"Resultado de la integral: {resultado}")
print(f"Error estimado: {error}")