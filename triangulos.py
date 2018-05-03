#ESTE PROGRAMA IDENTIFICA SI EL TIRANGULO INGRESADO
#ES INVALIDO,ISOSELES,ESCALENO O EQUILATERO

def es_triangulo(a,b,c):

    if int(a)> int(b) + int(c):
        return False
    elif int(b)> int(a) + int(c):
        return False
    elif int(c)> int(b) + int(a):
        return False
    else:
        return True

def tipo_triangulo(a,b,c,triangulo):
    if triangulo == True:
        if a == b and b == c:
            return 'El triangulo  es equilatero'
        elif (a == b and  b!=c) or (b == c and a!=c) or (a == c and a!=b):
            return 'El triangulo  es isoseles'
        else:
            return 'El triangulo  es escaleno'

    else:
        return 'No es un triangulo valido.'

a=raw_input("Ingrese a:\n")
b=raw_input("Ingrese b:\n")
c=raw_input("Ingrese c:\n")

print tipo_triangulo(a,b,c,es_triangulo(a,b,c))
raw_input()
