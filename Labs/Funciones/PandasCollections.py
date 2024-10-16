import pandas as pd
import io
from collections import Counter

ventasdf = pd.read_csv("SalesJan2009.csv")
# ventasdf1 = pd.read_csv("https://raw.githubusercontent.com/arleserp/MinTIC2022/master/files/SalesJan2009.csv")
# print(ventasdf)
# print(ventasdf1)
ventasdf.head(3)

cp = Counter(ventasdf["Country"])
print(cp.most_common(3))
# Imprimimos los 3 países más comunes en la columna "Country" y el número de veces que aparecen.
# `most_common(3)`  cp = Counter(ventasdf["Country"]) una lista de tuplas con los 3 elementos más frecuentes y sus frecuencias.


cv = Counter(ventasdf["Payment_Type"])
# Utilizamos `Counter` nuevamente para contar las ocurrencias de cada valor en la columna "Payment_Type", que probablemente contiene los métodos de pago (como tarjeta de crédito, PayPal, etc.).

print(cv.most_common(3))
# Imprimimos los 3 métodos de pago más comunes en la columna "Payment_Type" y el número de veces que aparecen.
# `most_common(3)` devuelve una lista de tuplas con los 3 métodos de pago más frecuentes y sus frecuencias.
