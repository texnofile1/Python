#ESTE PROGRAMA CALCULA LA GANANCIA DE DOS TRANSBORDADORES


#VARIABLES
global T1
global T2
T1=150
T2=100
PRECIO_MOTOS=5000
PRECIO_AUTOS=12000
PRECIO_BUSES=34300
cantidadAutos=0
cantidadBuses=0
cantidadMotos=0
gananciaT1=0
gananciaT2=0
pesoVehiculo=0

tipoVehiculo=0


#FUNCIONES
def iniciarPrograma():

    print "Ingrese vehiculo...\nvehiculo en plataforma calculando peso...\n"
    pesoVehiculo=int(float(raw_input("Ingrese el peso de su vehiculo (Toneladas):\n")))
    return asignarTrans(pesoVehiculo)



#ENVIA VEICULO A TRANSFER
def asignarTrans(pesoVe):
    if T2 > T1:
        if pesoVe <= T2:
            print "Ingresare en la plataforma 2"
            return descontarDinero(pesoVe,T2)
         #FINALIZAR EL PROGRAMA#   
        else:
            return finalizarPrograma()
    elif pesoVe <=T1:
        print "Ingresare en la plataforma 1"
        return descontarDinero(pesoVe,T1)
    #FINALIZAR EL PROGRAMA
    else:
        return finalizarPrograma()

        
        
def descontarDinero(pesoVe, trans):
    global cantidadMotos
    global cantidadAutos
    global cantidadBuses
    global gananciaT1
    global gananciaT2
    global T2
    global T1
    print "Ingrese tipo vehiculo:\n"
    tipoVehiculo=str(raw_input("Seleccione:\nM para motos\nA para autos\nB para buses\n")).lower()
    if tipoVehiculo == "m":
        cantidadMotos=cantidadMotos +1
        if trans ==T2:
            gananciaT2=gananciaT2+1*PRECIO_MOTOS
            T2=T2-pesoVe
        
        else:
            gananciaT1=gananciaT1+1*PRECIO_MOTOS
            T1=T1-pesoVe

    elif tipoVehiculo == "a":
        cantidadAutos=cantidadAutos +1
        if trans ==T2:
            gananciaT2=gananciaT2+1*PRECIO_AUTOS
            T2=T2-pesoVe
        
        else:
            gananciaT1=gananciaT1+1*PRECIO_AUTOS
            T1=T1-pesoVe
    
            
    elif tipoVehiculo  =="b":
        cantidadBuses=cantidadBuses +1
        if trans ==T2:
            gananciaT2=gananciaT2+1*PRECIO_BUSES
            T2=T2-pesoVe
        else:
            gananciaT1=gananciaT1+1*PRECIO_BUSES
            T1=T1-pesoVe
   
    if (T1==0) or (T2==0):
        return finalizarPrograma() 
    else:
        return iniciarPrograma()   
      
   

    
def finalizarPrograma():
    print "Ambos Transfer comenzaran su recorrido:\n"
    print "Las Ganancias de T1 fueron:%i\nLas Ganancias de T2 fueron:%i\n"%(gananciaT1,gananciaT2) 
    print "Sus Pesos son:\nT1:%i\nT2:%i\n"%(150-T1,100-T2)
    print "Ingresaran %i vehiculos a chiloe.\n"%(cantidadBuses+cantidadMotos+cantidadAutos)
    return raw_input()

#BLOQUE PRINCIPAL

iniciarPrograma()




