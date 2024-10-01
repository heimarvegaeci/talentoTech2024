def mezclar_diccionarios(diccionario1, diccionario2):
    diccionario_mezclado = diccionario2.copy()
    diccionario_mezclado.update(diccionario1)
    return diccionario_mezclado

def verificar_diccionarios(diccionario1, diccionario2):
    for clave, valor in diccionario1.items():
        if clave not in diccionario2 or diccionario2[clave] != valor:
            return False
    return True

def imprimir_numeros_ascendentes(diccionario):
    enteros = []
    flotantes = []

    for valor in diccionario.values():
        if isinstance(valor, int):
            enteros.append(valor)
        elif isinstance(valor, float):
            flotantes.append(valor)

    enteros.sort()
    flotantes.sort()

    print("Enteros:", enteros)
    print("Flotantes:", flotantes)

# Ejemplo de uso
mi_diccionario = {
    'a': 5,
    'b': 3.2,
    'c': 7,
    'd': 1.5,
    'e': 2,
    'f': 4.8
}

imprimir_numeros_ascendentes(mi_diccionario)

def imprimir_nombres(lista_personas):
    for persona in lista_personas:
        print(persona["nombre"])

# Ejemplo de uso
personas = [
    {"nombre": "Pedro", "Apellido": "Perez", "edad": 100},
    {"nombre": "Maria", "Apellido": "Gomez", "edad": 30},
    {"nombre": "Juan", "Apellido": "Lopez", "edad": 25}
]

imprimir_nombres(personas)

def imprimir_nombres_apellidos_rango_edad(lista_personas, edad_min, edad_max):
    for persona in lista_personas:
        if edad_min <= persona["edad"] <= edad_max:
            print(f'{persona["nombre"]} {persona["Apellido"]}')

# Ejemplo de uso
imprimir_nombres_apellidos_rango_edad(personas, 20, 50)

def contar_ocurrencias(cadena):
    ocurrencias = {}
    for letra in cadena:
        if letra in ocurrencias:
            ocurrencias[letra] += 1
        else:
            ocurrencias[letra] = 1
    return ocurrencias

# Ejemplo de uso
cadena = "abracadabra"
print(contar_ocurrencias(cadena))