#Lanzamientos de excepciones por parte nuestra en forma intencionada. Uilizo la sentencia RAISE

def evaluaEdad(edad):

if edad<0:
	raise TypeError("No se permiten edades negativas") #Puedo personalizar el mensaje del error que estoy mostrando con la excepcion raise

	if edad<20:
		return("Eres muy joven")
	elif edad<40:
		return("Eres joven")
	elif edad<65:
		return("Eres maduro")
	else edad<100:
		return("Cuidate...")

print(evaluaEdad(18))


