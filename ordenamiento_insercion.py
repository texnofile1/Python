"""
lista.append() añade al final
sort() ordena
reverse() invierte sentido
insert(indice, valor) insertar

pop() remover elemento
count(valor) contar cuantas veces se repite valor
clear() limpiar lista
"""

def RANKING(REGIONES):
    lista_final=list()
    anterior=0
    i=-1
    nombre_region=""
    for region in REGIONES:
        nombre_region,n_region,anno,mes,dia,estadisticas=region
        P_difuntas=estadisticas[2]
        i+=1
        if P_difuntas>=anterior:
            lista_final.insert(i,(nombre_region,P_difuntas))
            anterior=P_difuntas
        elif P_difuntas <anterior:
            for j in range(len(lista_final)):
                if P_difuntas < lista_final[j][1]:
                    lista_final.insert(j,(nombre_region,P_difuntas))
                    break
    return lista_final

a=[('valpo',5,2018,'abril',18,(12,15,30)),('trole',5,2018,'abril',18,(12,15,10)),('vdaspo',5,2018,'abril',18,(12,15,60)),('MATAYA',5,2018,'abril',18,(12,15,6))]


ranking=RANKING(a)
print ranking
