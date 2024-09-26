# importao las clase Empleado y ConstantesNomina
from Empleado import Empleado
from ConstantesNomina import ConstantesNomina
import pandas as pd

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
    
    # Metodo para calcular la salud por parte de la empresa
    def calcular_salud_empresa(self, base_deduccion):
        deduccion_salud_empresa = base_deduccion * ConstantesNomina.SALUD_EMPRESA
        return deduccion_salud_empresa
    
    #Metodo para calcular la pensión del empleado
    def calcular_pension_empleado(self,base_deduccion):
        deduccion_salud = base_deduccion * ConstantesNomina.PENSION_EMPLEADO
        return deduccion_salud
    
    # Metodo para calcular la pensión por parte de la empresa
    def calcular_salud_empresa(self, base_deduccion):
        deduccion_pension_empresa = base_deduccion * ConstantesNomina.PENSION_EMPRESA
        return deduccion_pension_empresa
    
    # Metodo para calcular el SENA
    def calcular_sena(self, base_deduccion):
        deduccion_sena = base_deduccion * ConstantesNomina.SENA
        return deduccion_sena

    # Metodo para calcular la Caja de Compensación Familiar (CCF)
    def calcular_ccf(self, base_deduccion):
        deduccion_ccf = base_deduccion * ConstantesNomina.CCF
        return deduccion_ccf

    # Metodo para calcular el Instituto Colombiano de Bienestar Familiar (ICBF)
    def calcular_icbf(self, base_deduccion):
        deduccion_icbf = base_deduccion * ConstantesNomina.ICBF
        return deduccion_icbf
    
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
    
    # Metodo para calcular cesantias
    def calcular_cesantias(self, total_devengado):
        cesantias = total_devengado * ConstantesNomina.CESANTIAS
        return cesantias

    # Metodo para calcular intereses de cesantias
    def calcular_intereses_cesantias(self, cesantias):
        intereses_cesantias = cesantias * ConstantesNomina.INTERESES_CESANTIAS
        return intereses_cesantias

    # Metodo para calcular la prima
    def calcular_prima(self, total_devengado):
        prima = total_devengado * ConstantesNomina.PRIMA
        return prima
    
    # Metodo para calcular las vacaciones
    def calcular_vacaciones(self, total_devengado):
        vacaciones = total_devengado * ConstantesNomina.VACACIONES
        return vacaciones
    
# Ejemplo de uso
def mostrar_datos(calculos_nomina, salario_basico, auxilio_transporte, horas_extras, total_devengado, salud_empleado, pension_empleado, fondo_solidaridad, valor_retefuente, deducciones, salud_empresa, pension_empresa, sena, icbf, ccf, total_parafiscales, cesantias, intereses_cesantias, prima, vacaciones, total_prestaciones, total_nomina):
    print("\n========= Datos del Empleado =========")
    print(calculos_nomina.empleado)
       
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

    print("\n========= Parafiscales =========")
    print(f"Salud Empresa: {calculos_nomina.formatear_valor(salud_empresa)}")
    print(f"Pension Empresa: {calculos_nomina.formatear_valor(pension_empresa)}")
    print(f"SENA: {calculos_nomina.formatear_valor(sena)}")
    print(f"ICBF: {calculos_nomina.formatear_valor(icbf)}")
    print(f"CCF: {calculos_nomina.formatear_valor(ccf)}")
    print(f"Total Parafiscales: {calculos_nomina.formatear_valor(total_parafiscales)}")

    print("\n========= Prestaciones =========")
    print(f"Cesantias: {calculos_nomina.formatear_valor(cesantias)}")
    print(f"Intereses Cesantias: {calculos_nomina.formatear_valor(intereses_cesantias)}")
    print(f"Prima: {calculos_nomina.formatear_valor(prima)}")
    print(f"Vacaciones: {calculos_nomina.formatear_valor(vacaciones)}")
    print(f"Total Prestaciones: {calculos_nomina.formatear_valor(total_prestaciones)}")

    print(f"Total nómina: {calculos_nomina.formatear_valor(total_nomina)}")

if __name__ == "__main__":

    empleados = [
        Empleado(54987654, "Catalina Hernandez", 6000000, 22, 10, 5, 2, 20, 18),
        Empleado(12345678, "Juan Perez", 4500000, 30, 5, 3, 1, 15, 10),
        Empleado(87654321, "Maria Gomez", 7000000, 28, 8, 4, 3, 25, 20)
    ]
    datos_nomina = []
    for empleado in empleados:
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

        #Calculando parafiscales
        salud_empresa = calculos_nomina.calcular_salud_empresa(base_deducciones)
        pension_empresa = calculos_nomina.calcular_salud_empresa(base_deducciones)
        sena = calculos_nomina.calcular_sena(base_deducciones)
        icbf = calculos_nomina.calcular_icbf(base_deducciones)
        ccf = calculos_nomina.calcular_ccf(base_deducciones)
        total_parafiscales = salud_empresa + pension_empresa + sena + icbf + ccf

        #Calculando prestaciones
        cesantias = calculos_nomina.calcular_cesantias(total_devengado)
        intereses_cesantias = calculos_nomina.calcular_intereses_cesantias(cesantias)
        prima = calculos_nomina.calcular_prima(total_devengado)
        vacaciones = calculos_nomina.calcular_vacaciones(total_devengado)
        total_prestaciones = cesantias + intereses_cesantias + prima + vacaciones

        salario_neto = total_devengado - deducciones

        #Calcula el total de la nomina
        total_nomina = total_devengado + total_prestaciones + total_parafiscales

        mostrar_datos(calculos_nomina, salario_basico, auxilio_transporte, horas_extras, total_devengado, salud_empleado, pension_empleado, fondo_solidaridad, valor_retefuente, deducciones, salud_empresa, pension_empresa, sena, icbf, ccf, total_parafiscales, cesantias, intereses_cesantias, prima, vacaciones, total_prestaciones, total_nomina)

        datos_nomina.append({
                "Cedula": empleado.cedula,
                "Nombre": empleado.nombre,
                "Salario Básico": salario_basico,
                "Auxilio Transporte": auxilio_transporte,
                "Horas Extras": horas_extras,
                "Total Devengado": total_devengado,
                "Salud Empleado": salud_empleado,
                "Pensión Empleado": pension_empleado,
                "Fondo Solidaridad": fondo_solidaridad,
                "Retefuente": valor_retefuente,
                "Total Deducciones": deducciones,
                "Salud Empresa": salud_empresa,
                "Pensión Empresa": pension_empresa,
                "SENA": sena,
                "ICBF": icbf,
                "CCF": ccf,
                "Total Parafiscales": total_parafiscales,
                "Cesantías": cesantias,
                "Intereses Cesantías": intereses_cesantias,
                "Prima": prima,
                "Vacaciones": vacaciones,
                "Total Prestaciones": total_prestaciones,
                "Salario Neto": salario_neto,
                "Total Nómina": total_devengado + total_prestaciones + total_parafiscales
            })
        
    dtFrame = pd.DataFrame(datos_nomina)
    dtFrame.to_excel('Nomina.xlsx', index=False)