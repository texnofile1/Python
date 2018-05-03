##ESTE PROGRAMA CALCULA EL NUMERO MAYOR DE LOS INGRESADOS##

numero=int(raw_input("Ingrese cantidad de numeros a evaluar:\n"))

i=0
mayor=0
while i < numero:
    x=int(raw_input("Ingrese numero:\n"))
    if mayor < x:
        mayor = x
    i += 1
print "El Numero mayor es:",mayor    


raw_input()
