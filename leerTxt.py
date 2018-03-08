# -*- coding: cp1252 -*-
"""ESTE PROGRAMA LEE LAS LINEAS DE UN ARCHIVO DE TEXTO Y LAS
IMPRIME POR PANTALLA, DE MOMENTO EL ARCHIVO A LEER DEBE ESTAR
EN LA MISMA CARPETA QUE ESTE SCRIPT EN PYTHON EN FORMATO TXT"""


#ENTRADA:RECIVE EL NOMBRE DEL ARCHIVO JUNTO A SU EXTENCION
#PROCESO:LEE LAS LINEAS DEL ARCHIVO
#SALIDA:IMPRIME LAS LINEAS DEL ARCHIVO POR CONSOLA
def leerArchivo(archivo):
        #EL MODO SERA r (READ, w(WRITE), a(APPEND)
        archivo=open(archivo,'r')
        for linea in archivo.readlines():
            print linea
        archivo.close()
        return "Se ha leido correctamente su documento %s \n"



#ENTRADA
archivo=str(raw_input("Ingrese el nombre del archivo a leer: \n"))
#PROCESO
resultado=leerArchivo(archivo)
#SALIDA
print resultado %archivo

