produccion="produccion.txt"
paises="paises.txt"


#funcion que compara ides del archivo paises, busca datos y extrae
def leer_archivos(produccion, paises):
    paises=open(paises,"r")#tambien se puede omitir "r" al leer
    cat=set()#utilizamos propiedad de los conjuntos para obtener areas de paper
    #contadores
    total=0
    maximo=0
    minimo=1e1000
    #por cada linea en pais buscamos el ide
    for linea in paises:
        codigo,pais=linea.strip().split(";")
        #abrimos texto que contiene produccion
        produccion1=open(produccion,"r")
        for dato in produccion1:
            ide,cate,cant=dato.strip().split(",")
            cant=int(cant)
            #si es el que buscamox extraemos la informacion
            if codigo == ide:
                total+=cant
                cat.add(cate)
                if int(cant)> maximo:
                    maximo=cant
                elif cant < minimo:
                    minimo=cant
        escribir_datos(pais,total,maximo,minimo,len(cat))
        cat=set()
        total=0
        maximo=0
        minimo=1e1000
        #cerramos archivo produccion
        produccion1.close()
    #cerramos archivo paises
    paises.close()
    return

#funcion que da el formato de salida correspondiente
def escribir_datos(pais,total,maximo,minimo,diversidad):
    archivo=open("informe.txt", "a")
    archivo.write("Pais: {0}\nTotal: {1}\nMaximo: {2}\nMinimo: {3}\nDiversidad: {4}\n\n".format(pais.upper(),total,maximo,minimo,diversidad))
    archivo.close()
    return



#MAIN#

leer_archivos(produccion,paises)

print "REALIZADO..."
raw_input()
