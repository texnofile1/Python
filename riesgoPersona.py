#CALCULA RIESGO PERSONA POR IMC Y EDAD#
def calcular_imc(peso,estatura):
    imc=float(peso)/(float(estatura)**2)
    return imc


def calcular_riesgo(imc,edad):
    if imc >= 22.0:
        if int(edad) < 45:
            return 'Medio'
        else:
            return 'Alto'
    else:
        if int(edad) < 45:
            return 'Bajo'
        else:
            return 'Medio'
estatura=raw_input("Ingrese Estatura:\n")
peso=raw_input("Ingrese Peso:\n")
edad=raw_input("Ingrese Edad:\n")

print "Su condicion de riesgo es: ",calcular_riesgo(calcular_imc(peso,estatura),edad)

raw_input()
