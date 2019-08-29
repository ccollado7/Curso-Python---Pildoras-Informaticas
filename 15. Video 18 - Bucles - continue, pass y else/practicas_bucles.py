#Uso de la sentencia continue

for letra in "Python": #Creo un Bucle

	if letra =="h":#Durante la ejecucion del bucle si se encuentra la letra h se ignora el print que viene a continuacion
		continue

	print("Viendo la letra: " + str(letra))