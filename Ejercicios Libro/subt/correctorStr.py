subtitulos="subtitulos.str"

#00:00:29,533 --> 00:00:31,501
#(29.533,31.501)
def formatear_tiempo(tiempo):
    formato=[]
    tiempo=tiempo.strip().split("-->")
    for elemento in tiempo:
        hr,mi,se=elemento.strip().split(":")
        se=se.split(",")
        formato.append(float(hr+mi+se[0]+"."+se[1]))
    return tuple(formato)

#00:00:36,340 --> 00:00:42,639
#36.231
def cambiar_linea(linea,nuevoInicio):
    inicio,fin =linea.strip().split("-->")
    faltantes=10-len(str(nuevoInicio))
    nuevoInicio="0"*faltantes+str(nuevoInicio)
    nuevoInicio=nuevoInicio[:2]+":"+nuevoInicio[2:4]+":"+nuevoInicio[4:6]+","+nuevoInicio[7:]
    linea=nuevoInicio+" --> "+fin
    return linea

def escribir(nombre,texto):
    archivo=open(nombre,"w")
    archivo.write(texto)
    archivo.close()
    return "FINALIZADO..." 

def identificar_error(subtitulos):
    tiempo_anterior=1e10000
    texto=""
    valor=False
    archivoStr=open(subtitulos,"r")
    for linea in archivoStr:
        if linea.count(":") > 1:
            inicio, fin=formatear_tiempo(linea)
            if inicio < tiempo_anterior:
                linea =cambiar_linea(linea,tiempo_anterior)
                texto+=linea+"\n"
                tiempo_anterior=fin
                continue
            else:
                tiempo_anterior=fin
        texto+=linea
    archivoStr.close()
    return escribir("subtitulos2.str",texto)


print identificar_error(subtitulos)