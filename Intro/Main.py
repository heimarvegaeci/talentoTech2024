from Calculos import Calculos

try:
    lado = float(input("Ingrese el lado de la figura: "))
    figura = Calculos(lado)
    superficie = figura.calcular_superficie()
    perimetro = figura.calcular_perimetro()

    print("La superficie de la figura es:", superficie)
    print("El perímetro de la figura es:", perimetro)
except ValueError:
    print("Por favor, ingrese un número válido.")
except AttributeError:
    print("Error: Asegúrese de que los métodos calcular_superficie y calcular_perimetro estén definidos en la clase Calculos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")