## PROGRAMITA ADMITE O RECHAZA VISITAS##

def verifica(pais):
    lista_baneados="IRN,SYR,YEM,SDN,SOM"
    if pais in lista_baneados:
        return False
    return True

def ingresos(paises):
    pais=""
    i=0
    while i<len(paises):
        if paises[i]!=",":
            pais+=paises[i]
        else:
            resultado=verifica(pais)
            print "El pais",pais,resultado
            pais=""
        i+=1
    resultado=verifica(pais)
    print "El pais",pais,resultado    
    return




paises=raw_input("Ingrese cadena:")
ingresos(paises)
