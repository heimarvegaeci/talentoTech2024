import numpy as np
import matplotlib.pyplot as plt

# Generar 50 números entre 0 y 2
x = np.linspace(0, 2, 50)

# Funciones
y1 = x
y2 = x**2
y3 = x**3
y4 = np.log(x + 1)  # Se suma 1 para evitar log(0)

# Crear la gráfica
plt.figure()

# Gráfica lineal
plt.plot(x, y1, label='Lineal')

# Gráfica cuadrática
plt.plot(x, y2, label='Cuadrática')

# Gráfica cúbica
plt.plot(x, y3, label='Cúbica')

# Gráfica logarítmica
plt.plot(x, y4, label='Logarítmica')

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()