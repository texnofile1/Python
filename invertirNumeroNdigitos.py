#ESTE PROGRAMA INVIERTE UN NUMERO DE N DIGITOS#

def invertir_numero(numero):
    nuevoNumero=''
    i=0
    while len(numero)>i:
        nuevoNumero += numero[len(numero)-i-1]
        i +=1
    return nuevoNumero


numerito=raw_input("Ingrese Numero a invertir:\n")
print "El nuevo numero es: ",invertir_numero(numerito)
raw_input()
