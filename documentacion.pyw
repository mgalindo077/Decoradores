class Areas:
	""" Esta clase calcula las areas de diferentes figuras geometricas"""

	def areaCuadrado(Base):
		""" Calcula el area de un cuadrado, 
		elevando al cuadrado el parametro recibido"""
		return "El area del cuadrado es: " + str(Base*Base)

	def areaTriangulo(Base, Altura):
		""" Calcula el area de un triangulo,
		utilizando los parametros base y altura de referencia"""
		return "El area del triangulo es: "+ str((Base*Altura)/2)


print(Areas.areaCuadrado(3))
print(Areas.areaTriangulo(2,7))
print(Areas.areaCuadrado.__doc__)

help(Areas.areaCuadrado)
help(Areas.areaTriangulo)

help(Areas)