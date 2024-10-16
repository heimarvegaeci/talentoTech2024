# Solución Ejercicio 2
from scipy import optimize

# Definimos la función
def f(x):
    return x**4 - 3*x**3 + 2

# Encontramos el mínimo
resultado = optimize.minimize(f, x0=0)
print(f"Mínimo en: {resultado.x}")