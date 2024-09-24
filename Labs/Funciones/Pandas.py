import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'María'],
    'Edad': [28, 34, 29, 42],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)
print(df)

# Filtrar datos
mayores_30 = df[df['Edad'] > 30]
print(mayores_30)

# Calcular la edad promedio
edad_promedio = df['Edad'].mean()
print(f"La edad promedio es: {edad_promedio}")