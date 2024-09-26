class Empleado:
    def __init__(self, cedula: int, nombre: str, sueldo: float, dias: float, horas_recargo_nocturno: float, horas_extras_diurnas: float, horas_extras_nocturnas: float, horas_extras_dominicales_diurnas: float,horas_extras_dominicales_nocturnas: float):
        self.cedula = cedula
        self.nombre = nombre
        self.sueldo = sueldo
        self.salario_base = 0
        self.dias = dias
        self.horas_recargo_nocturno = horas_recargo_nocturno
        self.horas_extras_diurnas = horas_extras_diurnas
        self.horas_extras_nocturnas = horas_extras_nocturnas        
        self.horas_extras_dominicales_diurnas = horas_extras_dominicales_diurnas
        self.horas_extras_dominicales_nocturnas = horas_extras_dominicales_nocturnas

    def __str__(self):
        return (f"  Cédula: {self.cedula}\n"
            f"  Nombre: {self.nombre}\n"
            f"  Sueldo: {self.sueldo:.2f}\n"
            f"  Días trabajados: {self.dias}\n"
            f"  Horas recargo nocturno: {self.horas_recargo_nocturno}\n"
            f"  Horas extras diurnas: {self.horas_extras_diurnas}\n"
            f"  Horas extras nocturnas: {self.horas_extras_nocturnas}\n"
            f"  Horas extras dominicales diurnas: {self.horas_extras_dominicales_diurnas}\n"
            f"  Horas extras dominicales nocturnas: {self.horas_extras_dominicales_nocturnas}")