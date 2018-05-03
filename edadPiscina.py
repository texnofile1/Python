#ESTE PROGRAMA CALCULA LA EDAD PROMEDIO DE USUARIOS DE PISCINA#
total=0
promedio=0
ninos=0
adultos=0
estudiantes=0
verdad=True
while verdad:

    edad=raw_input("Ingresa edad:")
    if edad !='0':
        promedio+=int(edad)
        total+=1
        if int(edad) <18:
            ninos =ninos+1
        
        elif int(edad) <25 and int(edad) >18:
            estudiantes=estudiantes+1

        else:
            adultos=adultos+1

    else:
     verdad=False
    
print "Total Personitas:  ",total
print "Promedio:  ",float(promedio/total)
print "Cantidad Niños:  ", ninos
print "Cantidad Adultos  :", adultos
print "Cantidad Estudiantes:  ", estudiantes


raw_input()
