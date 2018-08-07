#definimos pronombres
pronombres=["yo","tu","el","nosotros", "vosotros", "ellos"]

#diccionarios respecto a pronombres y terminacion
dic_ar={"yo":"o","tu":"as","el":"a","nosotros":"amos", "vosotros":"ais", "ellos":"an"}
dic_er={"yo":"o","tu":"es","el":"e","nosotros":"emos", "vosotros":"eis", "ellos":"en"}
dic_ir={"yo":"o","tu":"es","el":"e","nosotros":"imos", "vosotros":"is", "ellos":"en"}

#cortamos ultimas letras del verbo y concatenamos conjugacion
def conjugar(verbo):
    if verbo[-2:]=="ar":
        for pronombre in pronombres:
            #print pronombre+" "+verbo[:-2]+dic_ar[pronombre]
            salida(pronombre,verbo[:-2],dic_ar[pronombre])
    elif verbo[-2:]=="er":
        for pronombre in pronombres:
            #print pronombre+" "+verbo[:-2]+dic_er[pronombre]
            salida(pronombre,verbo[:-2],dic_er[pronombre])
    else:
        for pronombre in pronombres:
            #print pronombre+" "+verbo[:-2]+dic_ir[pronombre]
            salida(pronombre,verbo[:-2],dic_ir[pronombre])
            hola=5
    return

#se da formato de salida e imprime en pantalla
def salida(pronombre, verbo, conjugado):
    print "{} {}{}".format(pronombre,verbo,conjugado)
    return

#MAIN#
verbo=raw_input("Ingrese verbo: ")
conjugar(verbo)
