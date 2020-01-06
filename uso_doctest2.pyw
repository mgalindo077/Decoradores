import math

def raizCuadrada(numerosLista):

	"""
	La funcion devuelve una lista con la raiz
	cuadrada de los elementos numericos recibidos

	>>> lista=[]
	>>> for i in [4, 9, 16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0] 	

	>>> lista=[]
	>>> for i in [4, -9, 16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
		...
    ValueError: math domain error

	"""

	return [math.sqrt(n) for n in numerosLista]


print(raizCuadrada([9,16,25,36]))
#import doctest
#doctest.testmod()