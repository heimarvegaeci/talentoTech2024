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
        return (f"Empleado(cedula={self.cedula}, nombre='{self.nombre}', sueldo={self.sueldo}, "
                f"dias={self.dias}, horas_recargo_nocturno={self.horas_recargo_nocturno}, "
                f"horas_extras_diurnas={self.horas_extras_diurnas}, horas_extras_nocturnas={self.horas_extras_nocturnas}, "
                f"horas_extras_dominicales_diurnas={self.horas_extras_dominicales_diurnas}, "
                f"horas_extras_dominicales_nocturnas={self.horas_extras_dominicales_nocturnas})")