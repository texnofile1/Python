


archivo_jugadores="jugadores.txt"
archivo_resultados="Resultados.txt"

def puntaje_final(nombre,archivo_jugadores,archivo_resultados):
    archivo_jugadores=open(archivo_jugadores)

    for linea in archivo_jugadores:
        rut,jugador=linea.strip().split("/")
        if jugador == nombre:
            rut=rut[:-2]+rut[-1:]
            rut=rut.split(".")
            rut="".join(rut)
            archivo_resultados=open(archivo_resultados)
            for resultados in archivo_resultados:
                ide,resultados=resultados.strip().split("-")
                if ide == rut:
                    v,e,d= resultados.split("/")
                    #print (ide , "Victoria: {0} pto, empate: {1} pto, derrota: {2} pto".format(int(v)*3,int(e)*1,d))
                    pujt=int(v)*3+int(e)*1+int(d)
                    return (pujt,ide)
            archivo_resultados.close()
    archivo_jugadores.close()
    return


def lugares(archivo_jugadores,archivo_resultados):
    archivo_jugadores1=open(archivo_jugadores)
    lista=[]
    for line in archivo_jugadores1:
        rut,ide=line.strip().split("/")
        lista.append(puntaje_final(ide,archivo_jugadores,archivo_resultados))
    archivo_jugadores1.close()
    lista.sort(reverse=True)
    return lista[:3]

print lugares(archivo_jugadores,archivo_resultados)
