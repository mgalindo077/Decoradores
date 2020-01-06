def compruebaMail(mailUsuario):
	"""
	la funcion comprueba la validez de una direccion de correo electronico

	>>> compruebaMail('mgalindo077@gmail.com')
	True

	>>> compruebaMail('mgalin@do077@gmail.com')
	False

	>>> compruebaMail('mgalindo077gmail.com@')
	False

	>>> compruebaMail('mgalindo077gmail.com')
	False

	"""

	arroba=mailUsuario.count('@')
	if (arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True

import doctest
doctest.testmod()