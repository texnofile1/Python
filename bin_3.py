#POSIBLE SOLUCION PROBLEMA 3#
##FUNCIONES##

def transformar(numerito):
    i=0
    numero=0
    largo=len(numerito)-1
    while i < len(numerito):
        numero+=int(numerito[largo-i])*(2**i)
        i+=1
    return numero

def es_par(numerito):
    if int(numerito) %2 == 0:
        return True
    return False

def largo_valido(numerito):
    if len(numerito)>=4 and len(numerito) <=8:
        return True
    else:
        return False

def caracteres_validos(numerito):
    i=0
    while i <len(numerito):
        if numerito[i] != '0' and numerito[i] != '1':
            return False
        i+=1
    return True


##PRINCIPAL##
n_pares=0
n_impares=0
n_totales=0
flag=True

while flag:
    valor=raw_input("Ingrese cadena de caracteres: ")
    if largo_valido(valor) == True and caracteres_validos(valor) == True:
        valor=transformar(valor)
        n_totales+=1
        print valor
        if es_par(valor):
            n_pares +=1
        else:
            n_impares+=1
    else:
        flag=False

print "Total",n_totales
print "Impares",n_impares
print "Pares",n_pares

raw_input()
