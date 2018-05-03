#ESTE PROGRAMA CAMBIA LAS VOCALES POR UNA I#



def birli(string):
    i=0
    while i<len(string):
        if string[i] == 'a' or string [i] =='e' or string [i] =='o' or string [i] =='u':
            string=string[:i]+"i"+string[i+1:len(string)]
        elif string[i] == 'A' or string [i] =='E' or string [i] =='O' or string [i] =='U':
            string=string[:i]+"I"+string[i+1:len(string)]
        i+=1
    return  string



frase=raw_input("Ingrese frase:\n")
print birli(frase)
raw_input()
