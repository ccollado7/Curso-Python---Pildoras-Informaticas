
#Creo la funcion generador

def devuelve_ciudades(*ciudades): #Cuando se coloca un * antes del nombre del argumento se indica que se recibiran un numero indeterminados de elementos
	for elemento in ciudades:
		yield (elemento)


#Creo un objeto generador

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelon","Bilbao","Valencia")

print(next(ciudades_devueltas)) #Accedo a la primera ciudad

print(next(ciudades_devueltas)) #Accedo a la segunda ciudad
