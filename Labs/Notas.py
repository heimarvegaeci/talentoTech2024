def CalcularNotas():
    #Obteniendo las notas
    nota1 = obtenerNota()
    nota2 = obtenerNota()
    nota3 = obtenerNota()
    nota4 = obtenerNota()
    
    #pesos de las notas
    PESO_NOTA1 = 0.05
    PESO_NOTA2 = 0.07
    PESO_NOTA3 = 0.12
    PESO_NOTA4 = 0.18

    notaEsperada = 4.0
    pesoNota5 = 1 - PESO_NOTA1 - PESO_NOTA2 - PESO_NOTA3 - PESO_NOTA4
    nota5 = (notaEsperada - (nota1 * PESO_NOTA1 + nota2 * PESO_NOTA2 + nota3 * PESO_NOTA3 + nota4 * PESO_NOTA4)) / pesoNota5
    print(f"Nota necesaria: {nota5:.2f} , Peso: {pesoNota5*100:.2f}%")
    

def obtenerNota():
    nota = float(input("Ingrese la nota : "))
    return nota

CalcularNotas()