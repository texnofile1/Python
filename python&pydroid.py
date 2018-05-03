#ESTE PROGRAMITA CALCULA LOS EQUIPOS CON FALLAS #

def equipos_con_fallas(datos):
    i=0
    a=0
    b=0
    while i<len(datos):    
        if datos[i] =='a':
            a+=1
        elif datos[i] =='b':
            b+=1
        i+=1
    a=str(a)
    b=str(b)
    a=(3-len(a))*'0'+a
    b=(3-len(b))*'0'+b
    return a+"-"+b

    




a=0
b=0
flag=True

while flag:
    venta=raw_input("Ingrese venta:")
    
    if venta != "fin" and venta != "FIN":
        total=len(venta)
        print equipos_con_fallas(venta)
        print "Total equipos : ", total
        a += int(equipos_con_fallas(venta)[:3])
        b += int(equipos_con_fallas(venta)[6:])
      
        

    else:
        flag=False
print "pyPhone fallas",a
print "pyPhone fallas",b
raw_input()

