"""
    CONTROL 2
    MATIA CORNEJO
    201873091-2
    PARALELO 1

"""
####################FUNCIONES##########################




#funcion que invoca a las demas funciones para luego ordenar de menor a mayor , retornado lista de menor a mayor
def  agregar_ventas(libros, titulos, ventas):
    ventas=formato_ventas(ventas)
    ventas=costo_titulo(ventas,libros)
    ventas=nombre_titulo(ventas,titulos)
    ventas.sort()
    return ventas




#funcion que da el formato a ventas, colocando la fecha en primer lugar, RETORNANDO LISTA ORDENADA
def formato_ventas(ventas):
    lista_formato=[]
    auxiliar=[]
    for elemento in ventas:
        id_venta,fecha,titulos=elemento
        auxiliar.append(fecha)
        auxiliar.append(id_venta)
        auxiliar.append(titulos)    
        lista_formato.append(tuple(auxiliar))
        auxiliar=list(auxiliar)
        auxiliar=[]
    return lista_formato




#funcion que busca el costo de cada libro, calcula el iva y luego lo suma a la totalidad, ingresando con formato
def costo_titulo(ventas,libros):
    lista_ventas=[]
    auxiliar=[]
    total_compra=0
    for venta in ventas:
        libros_compra=venta[2]
        for libro in libros_compra:
            for librito in libros:
                if libro   in librito:
                    total_compra+=librito[2]*1.19

        venta=list(venta)
        venta.insert(2,total_compra)
        total_compra=0
        lista_ventas.append(tuple(venta))
        venta=[]
    return lista_ventas





#busca el nombre de todos los titulos posibles en cada venta y los añade a la lista, sobre escribiendo el codigo del libro por el nombre
def nombre_titulo(ventas,titulos):
    auxiliar=[]
    lista_con_titulos=[]
    for elemento in ventas:
        elemento=list(elemento)
        for contador in range(len(elemento[3])):
            for nombre in titulos:
                if elemento[3][contador] in nombre:
                    auxiliar.append(nombre[0])
                    
        elemento[3]=auxiliar
        lista_con_titulos.append(tuple(elemento))
        auxiliar=[]

    return lista_con_titulos




#DATOS#
libros = [("np01","Nicanor Parra", 15500,"poesia"), ("np02", "Nicanor Parra", 12500,"poesia"), ("gm01", "Gabriela Mistral", 15500,"poesia"), ("ggm01", "Gabriel Garcia Marquez", 14500,"novela")]
titulos = [("Poemas y antipoemas", "np01"), ("Ecopoemas", "np02"), ("Tala", "gm01"), ("Cien anios de soledad", "ggm01")]
ventas = [("vta-101",(2018,1,27), ["np01","gm01"]), ("vta-102",(2018,1,25),["gm01","ggm01"]), ("vta-104",(2018,1,26), ["np01","np02"]), ("vta-106",(2018,1,27), ["np01","np02"])]

#MAIN#
ventas=agregar_ventas(libros,titulos,ventas)

print ventas
raw_input()
