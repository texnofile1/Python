# -*- coding: cp1252 -*-
"""ESTE PROGRAMA IDENTIFICA SI EL NUMERO INGRESADO ES MÁGICO
VALE DECIR QUE LA SUMA DE TODOS LOS DIVISORES DE SI MISMO EXCEPTO
EL MISMO NUMERO SEAN EL MISMO NUMERO Ej.: 6, sus divisores son 1+2+3=6"""

#ENTRADA:RECIVE UN NUMERO A EVALUAR
#PROCESO:CALCULA SUS DIVISORES Y EVALUA SU SUMA
#SALIDA:ENTREGA EL RESULTADO SI ES MAGICO O NO
def esMagico(numero):
    divisores=0
    contador=1
    while contador < numero:
        if numero % contador == 0:
            divisores+=contador
        contador+=1
    if divisores == numero:
        return ("El Numero %i es un numero Magico \n")%numero
    else:
        return ("El Numero %i no es un numero Magico \n")%numero


#ENTRADA
numero=int(raw_input("Ingrese el numero a evaluar: \n"))
#PROCESO
respuesta=esMagico(numero)
#SALIDA
print respuesta
