def rondas(lista_jugadores):
    lista_jugadores=lista_jugadores
    n_rondas=1
    lista_ganadores=[]
    while len(lista_jugadores)>1:
        print "\nRonda"+str(n_rondas)
        a=""
        b="" 
        for x  in range(len(lista_jugadores)):
            if x > len(lista_jugadores):
                break
            if x % 2 ==0:
                a=lista_jugadores[x]
                print "a."+lista_jugadores[x], "-",
                
            else:
                b=lista_jugadores[x]
                ganador=raw_input("b."+lista_jugadores[x]+":")
                lista_ganadores.append(ganador)        
        n_rondas+=1
        lista_jugadores=ganadores(lista_jugadores,lista_ganadores)
    
def ganadores(lista_jugadores,lista_ganadores):
    x=0
    for elemento in lista_ganadores:
        if elemento == "a":
            lista_jugadores.remove(x)
            x+=1
        else:
            lista_jugadores.remove(x)
            x+=1
    return lista_jugadores
    
    


lista_jugadores=list()

for x  in range(8):
    cantidad=x+1
    lista_jugadores.append(raw_input("Jugador "+str(cantidad)+": "))

rondas(lista_jugadores)
