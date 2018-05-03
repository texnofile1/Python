

def posibles_donadores(rut ,Donadores,Pacientes):
    donadores_final=[]
    donantes={'A':['A','O'],'O':['O'],'B':['B','O'],'AB':['AB','A','B','O']}
    datos=Pacientes[rut]
    nombre,edad,tipo_sangre=datos
    posibles=donantes[tipo_sangre]
    for rut_id, variables in Donadores.items():
            x,y,z=variables
            if z in posibles and rut_id != rut:
                donadores_final.append(rut_id)
    return donadores_final






Donadores = {"31412-2": ("Marcelo Lopez", 25, "O"), "13241-9": ("Alexis Sanchez", 29, "B"),"16565464-9": ("TROLO THE VIL", 29, "O")}
Pacientes = { "512392-4": ("Sofia Vega", 35, "B"), "123456-k": ("Kurt Cobain", 27,"O"),"12234236-k": ("ysel an", 27,"A")}
print Pacientes
rut=raw_input("Ingrese rut paciente:\n")
print posibles_donadores(rut,Donadores,Pacientes)
