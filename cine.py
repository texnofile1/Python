def precio_dia(dia):
    if dia == 'lunes' or dia =='martes':
        return 3000
    elif dia == 'miercoles':
        return 2000
    else:
        return 4000
def descuento(precio,socio,est):
    if socio == 's' and est== 's':
        return precio*0.9
    elif socio == 's' and est== 'n':
        return precio*0.8
    else:
        return precio


dia=raw_input("ingrese dia de venta:\n")
precio=precio_dia(dia.lower())
estreno=raw_input("Es estreno:\n")
socio=raw_input("Es socio:\n")
print "El valor es",descuento(precio,socio,estreno)


raw_input()
