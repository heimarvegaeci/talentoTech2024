# Solución Ejercicio 3
from scipy import interpolate
import numpy as np

# Datos
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 8, 27, 64])

# Interpolación cúbica
f_interp = interpolate.interp1d(x, y, kind='cubic')

# Interpolamos nuevos valores
x_new = np.linspace(0, 4, 10)
y_new = f_interp(x_new)
print(y_new)