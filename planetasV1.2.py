
##ESTE PROGRAMITA VE SI UN PLANETA ES HABITABLE##


def gravedad_habitable(densidad,volumen):
    masa=float(volumen)*float(densidad)
    if masa >=0.8 and masa <=1.2:
        return 1
    else:
        return 0

def distancia_habitable(coordenadas):
    distanciaX=""
    distancia=0.0
    i=0
    while i<len(coordenadas):
        if coordenadas[i]!=":":
            distanciaX+=coordenadas[i]
        else:
             distancia +=float(distanciaX)**2
             distanciaX=""

        i+=1
    distancia+=float(distanciaX)
    distancia=distancia**1/2

    if distancia >=0.8 and distancia <=3.0:
        return 1
    else:
        return 0




print "Ingrese los datos sobre el planeta de interes:\n"

densidad=raw_input("Densidad: ")
volumen=raw_input("Volumen: ")
coordenadas=raw_input("Coordenadas: ")
if densidad =='0' or volumen == '0':
    print "El programa ha finalizado con exito."
else:
    masa=gravedad_habitable(densidad,volumen)
    distancia=distancia_habitable(coordenadas)
    if masa == 1 and distancia==1:
        print "El planeta de interes es habitable!"
    else:
        print "El planeta de interes no es habitable!"
        
raw_input()
