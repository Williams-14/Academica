def SalaryWorkers(horas, diario, nombre):
    if diario < 150:
        semanal = ((diario * horas ) * .05) 
        neto = (diario * horas) - semanal
        print(f"El sueldo del empleado {nombre} despues de descuentos es:")
        return round(neto, 2)
    elif diario > 150 and diario < 300:
        semanal = ((diario * horas ) * .07)
        neto = (diario * horas) - semanal
        print(f"El sueldo del empleado {nombre} despues de descuentos es:")
        return round(neto, 2)
    elif diario > 300 and diario >= 450:
        semanal = ((diario * horas ) * .09) 
        neto = (diario * horas) - semanal
        print(f"El sueldo del empleado {nombre} despues de descuentos es:")
        return round(neto, 2)
    
empleados = SalaryWorkers (84, 17.33, "Williams")
print(empleados)

