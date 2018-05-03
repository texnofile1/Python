propiedades = [{"numero": 512, "bannos": 2, "habitaciones": 4, "amoblada": "no", "pisos": 2, "precio": 100000000},{"numero": 523242, "bannos": 2, "habitaciones": 3, "amoblada": "no", "pisos": 2, "precio": 100000000},{"numero": 545432, "bannos": 2, "habitaciones": 5, "amoblada": "no", "pisos": 2, "precio": 100000000},{"numero": 822, "bannos": 2, "habitaciones": 4, "amoblada": "no", "pisos": 2, "precio": 100000000},{"numero": 760, "bannos": 3, "habitaciones": 3, "amoblada": "si", "pisos": 1, "precio": 270000000}]

###Diccionario para propiedades###



####FUNCION QUE RECORRE LOS NUMEROS DE HABITACIONES Y GENERA DICCIONARIO PARA AGREGAR NUMERO DE LA PROPIEDAD###
def filtrar_habitaciones(propiedades):
    diccionario_habitaciones={}
    for diccionario in propiedades:
        n_habit=diccionario["habitaciones"]
        n_casa=diccionario["numero"]
        if n_habit in diccionario_habitaciones:
            valores=diccionario_habitaciones[n_habit]
            valores.append(n_casa)
            diccionario_habitaciones[n_habit]=valores
        else:
            listita=[]
            listita.append(n_casa)
            diccionario_habitaciones[n_habit]=listita
    return diccionario_habitaciones


print filtrar_habitaciones(propiedades)
