# importao las clase Empleado y ConstantesNomina

from Empleado import Empleado
from ConstantesNomina import ConstantesNomina

#Clase para realizar los calculos de nomina
class CalculosNomina:
    #Inicializo la clase
    def __init__(self, empleado):
        self.empleado = empleado

    #Metodo para calcular el salario
    def calcular_salario_basico(self):
        # Salario básico diario
        salario_diario = self.empleado.sueldo / 30
        # Salario basico
        salario_basico = salario_diario * self.empleado.dias
        return salario_basico
    
    #Metodo para calcular la salud del empleado
    def calcular_salud_empleado(self,base_deduccion):
        deduccion_salud = base_deduccion * ConstantesNomina.SALUD_EMPLEADO
        return deduccion_salud
    
    #Metodo para calcular la pensión del empleado
    def calcular_pension_empleado(self,base_deduccion):
        deduccion_salud = base_deduccion * ConstantesNomina.PENSION_EMPLEADO
        return deduccion_salud
    
    # Función para calcular el Fondo de Solidaridad y Fondo de Subsistencia
    def calcular_fondo_solidaridad_subsistencia(self,total_devengado):
        salarios_minimos = total_devengado / ConstantesNomina.SMLV
        if 4 <= salarios_minimos <= 16:
            porcentaje = 0.01
        elif 16 < salarios_minimos <= 17:
            porcentaje = 0.012
        elif 17 < salarios_minimos <= 18:
            porcentaje = 0.014
        elif 18 < salarios_minimos <= 19:
            porcentaje = 0.016
        elif 19 < salarios_minimos <= 20:
            porcentaje = 0.018
        elif salarios_minimos > 20:
            porcentaje = 0.02
        else:
            porcentaje = 0
        fondo = total_devengado * porcentaje
        return fondo

    # Función para calcular la retención en la fuente
    def calcular_retencion_fuente(self, taxable_base, uvt):
        if uvt <= 95:
            retencion = 0
        elif 95 < uvt <= 150:
            retencion = 0.19 * taxable_base
        elif 150 < uvt <= 360:
            retencion = 0.28 * taxable_base + (10 * ConstantesNomina.VALOR_UVT)
        elif 360 < uvt <= 640:
            retencion = 0.33 * taxable_base + (69 * ConstantesNomina.VALOR_UVT)
        elif 640 < uvt <= 945:
            retencion = 0.35 * taxable_base + (162 * ConstantesNomina.VALOR_UVT)
        elif 945 < uvt <= 2300:
            retencion = 0.37 * taxable_base + (268 * ConstantesNomina.VALOR_UVT)
        else:
            retencion = 0.39 * taxable_base + (770 * ConstantesNomina.VALOR_UVT)
        return retencion

    #Metodo para calcular auxilio de transporte
    def calcular_auxilio_transporte(self):
        if self.empleado.sueldo <= 2*ConstantesNomina.SMLV:
            auxilio_transporte = ConstantesNomina.AUX_TRANSPORTE/30*self.empleado.dias
        else:
            auxilio_transporte = 0
        return auxilio_transporte
    
    #Metodo para calcular horas extras
    def calcular_horas_extras(self):
        valor_hora = self.empleado.sueldo / 230  # Asumiendo 230 horas laborales al mes
        valor_recargo_nocturno = valor_hora * ConstantesNomina.P_HRN * self.empleado.horas_recargo_nocturno
        valor_extras_diurnas = valor_hora * ConstantesNomina.P_HED * self.empleado.horas_extras_diurnas
        valor_extras_nocturnas = valor_hora * ConstantesNomina.P_HEN * self.empleado.horas_extras_nocturnas
        valor_extras_dominicales_diurnas = valor_hora * ConstantesNomina.P_HEDD * self.empleado.horas_extras_dominicales_diurnas
        valor_extras_dominicales_nocturnas = valor_hora * ConstantesNomina.P_HEDN * self.empleado.horas_extras_dominicales_nocturnas
        total_horas_extras = valor_recargo_nocturno + valor_extras_diurnas + valor_extras_nocturnas + valor_extras_dominicales_diurnas + valor_extras_dominicales_nocturnas
        return total_horas_extras
    
    #Metodo utilitario para formatear el texto
    def formatear_valor(self, valor):
        return f"${valor:,.2f}"
    
    #Metodo para calcular el total devengado  
    def calcular_total_devengado(self, salario_base, auxilio_transporte, horas_extras):                
        return (salario_base + auxilio_transporte + horas_extras)
    
    
# Ejemplo de uso
if __name__ == "__main__":
    empleado = Empleado(54987654,"Catalina Hernandez",6000000,22,10,5,2,20,18)
    calculos_nomina = CalculosNomina(empleado)
    salario_basico = calculos_nomina.calcular_salario_basico()
    auxilio_transporte = calculos_nomina.calcular_auxilio_transporte()
    horas_extras = calculos_nomina.calcular_horas_extras()
    total_devengado = calculos_nomina.calcular_total_devengado(salario_basico, auxilio_transporte, horas_extras)

    #Calculando las deducciones
    base_deducciones = total_devengado - auxilio_transporte
    salud_empleado = calculos_nomina.calcular_salud_empleado(base_deducciones)
    pension_empleado = calculos_nomina.calcular_pension_empleado(base_deducciones)
    fondo_solidaridad = calculos_nomina.calcular_fondo_solidaridad_subsistencia(base_deducciones)
    
    taxable_base = (base_deducciones - salud_empleado - pension_empleado - fondo_solidaridad) * 0.75
    uvt = taxable_base / ConstantesNomina.VALOR_UVT

    valor_retefuente = calculos_nomina.calcular_retencion_fuente(taxable_base, uvt)

    deducciones = salud_empleado + pension_empleado + fondo_solidaridad + valor_retefuente

    salario_neto = total_devengado - deducciones

    print("\n========= Devengado =========")
    print(f"Salario Basico: {calculos_nomina.formatear_valor(salario_basico)}")
    print(f"Auxilio Transporte: {calculos_nomina.formatear_valor(auxilio_transporte)}")
    print(f"Horas Extras: {calculos_nomina.formatear_valor(horas_extras)}")
    print(f"Total Devengado: {calculos_nomina.formatear_valor(total_devengado)}")

    print("\n========= Deducciones =========")
    print(f"Salud: {calculos_nomina.formatear_valor(salud_empleado)}")
    print(f"Pension: {calculos_nomina.formatear_valor(pension_empleado)}")
    print(f"Fondo Solidaridad: {calculos_nomina.formatear_valor(fondo_solidaridad)}")
    print(f"Retefuente: {calculos_nomina.formatear_valor(valor_retefuente)}")
    print(f"Total Deducibles : {calculos_nomina.formatear_valor(deducciones)}")
    print(f"Salario Neto: {calculos_nomina.formatear_valor(salario_neto)}")