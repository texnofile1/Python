#ESTE PROGRAMA CALCULA EL TIEMPO DE VIAJE DE X TRAMOS#

horas=0
minutos=0
verdad=True
while verdad:
    x=raw_input('Duración del tramo:\n')

    if x!='0':
        horas += int(x)/60
        minutos += int(x)%60
    else:    
        verdad=False
        if minutos > 60:
            horas += minutos/60
            minutos= minutos%60
print 'Tiempo total de viaje :',(str(horas)+':'+str(minutos))

raw_input()


