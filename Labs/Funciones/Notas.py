def obtener_notas_estudiante():
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    return notas

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def main():
    estudiantes = 5
    promedios_estudiantes = []

    for i in range(estudiantes):
        print(f"\nEstudiante {i + 1}:")
        notas = obtener_notas_estudiante()
        promedio = calcular_promedio(notas)
        promedios_estudiantes.append(promedio)
        print(f"Promedio del estudiante {i + 1}: {promedio:.2f}")

    promedio_general = calcular_promedio(promedios_estudiantes)
    print(f"\nPromedio general del grupo: {promedio_general:.2f}")

if __name__ == "__main__":
    main()