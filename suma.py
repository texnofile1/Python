suma=0
verdad=True

while verdad:
    x=int(raw_input("Ingrese numero:\n"))
    if x==0:
        verdad=False
    suma += x    


print"El resultado es: ",suma

raw_input()    
