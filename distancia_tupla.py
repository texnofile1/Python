def distancia(p1, p2):
    x1, y1= p1
    x2, y2= p2
    dx = x2 - x1
    dy = y2 - y1
    return (dx ** 2 + dy ** 2) ** .5



def perimetro(l):
    distancia_valor=0
    i=1
    largo=len(l)
    for tupla in l:
        distancia_valor+=distancia(tupla,l[i%largo])
        i+=1
    return distancia_valor
    
    
p = [(4, 1), (7, 2), (7, 4), (5, 9)]
print perimetro(p)
    
