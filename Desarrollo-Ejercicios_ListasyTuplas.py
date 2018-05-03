a = [5, 1, 4, 9, 0]
print "Lista a considerar\na=", a,"\nHola soy: 'print a[3:10:2]'\n>>>>",a[3:10:2],"\nLo que hago es utilizar el operador 'Rebanador', para partir desde el indice 3 hasta el indice 10-1, es decir 9, luego imprimo los elementos de 2  en 2 y los que queden fuera me los salto.\n"
print "#"*70,"\n"
c = ('Donald', True, 'b')
print "Tupla a considerar\nc=",c ,"\nHola soy: 'print c[0][0]'\n>>>>",c[0][0],"\nLo que hago es ingresar en la tupla, posteriormente en la pocision 0 y luego en ese valor, nuevamente ingreso a la posicion 0, esto quiere decir que imprimo una D.\n"
print "#"*70,"\n"
a = [5, 1, 4, 9, 0]
e = ['a', a, 2 * a]
c=[[1, 2], [3, 4, 5], [6, 7]]
print "Listas a considerar:\na={0}\ne={1}\nc={2}".format(a,e,c),"\nHola soy: 'e[c[0][1]].count(5)'\n>>>>",e[c[0][1]].count(5),"\nLo que hago es entrar en la posicion 0 de c, luego ahi ubico el dato con posicion 1, este sera el 2, con eso entro en la posicion 2 de e, luego de eso accedo a el, la cual es la lista a y con la funcion count(valor), busco la cantidad de variables que son igual a ese valor.\n"
print "#"*70,"\n"
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato',
'jirafa', 'elefante']
print "Listas a considerar:\nc={0}\nd={1}".format(c,d),"\nHola soy: 'c[2:] + d[2:]'\n>>>>",c[2:] + d[2:],"\nLo que hago es recorrer lista c desde el indice  2 hasta el final, luego recorro d desde indice 2 hasta el final y las concateno.\n"
print "#"*70,"\n"
x, y = ((27, 3), 9)
z, w = x
print "Tuplas a considerar:\nx, y = ((27, 3), 9)\nz, w = x\nHola soy y+w:\n>>>>",y+w,"\nLo que hago es desempaquetar los datos, en las variables x,y luego desempaqueto, la tupla x en z,w, posteriormente sumo y + w y eso es 12.\n"
print "#"*70,"\n"
a = (2, 10, 1991)
b = (25, 12, 1990)
print str(a + b)[2]
raw_input()
