def imprimir_receta(receta):
    archivo=open("recetario.txt","r")
    for line in archivo:
        line=line.strip().split(",")
        if line[0] == receta:
            print receta
            datos=""
            line=line[1:]
            for i in range(len(line)):
               # print line[i]
                if (i+1) % 2 == 0:
                    print datos + line[i]
                    datos=""
                else:
                    datos+=line[i]+" - "
    archivo.close()
    print "No existe"
    return
while True:
    receta=raw_input("Ingrese una receta: ")
    imprimir_receta(receta)
