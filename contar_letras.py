

def contar_letras(string):
    listita=[]
    for valor in string:
        tupla=valor, string.count(valor)
        if tupla not in listita:
            listita.append(tupla)

    return dict(listita)

a = contar_letras('entretener')
print a
