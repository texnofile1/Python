##ESTE PROGRAMA DETERMINA SI LA ECUACION INGRESADA POSEE SOLUCIOM##
print("Este programa resuelve ecuaciones de la forma ax+b=0\n")
a=raw_input("Ingrese el coeficienta 'a' de ax+b: \n")
b=raw_input("Ingrese el coeficienta 'b' de ax+b: \n")

if a == '0' and b == '0':
    print 'No hay solucion unica'
elif a == '0' and b != '0':
    print 'Sin solucion'
else:
    x=-1*(float(b)/float(a))
    print 'La solucion es x igual:',x
raw_input()    
