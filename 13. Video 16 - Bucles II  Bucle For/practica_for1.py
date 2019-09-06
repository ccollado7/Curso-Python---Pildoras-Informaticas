#Analisis de la validez de una direccion de e-mail en funcion de la presencia o no de la letra @

valido = False #Inicializo la variable valido

email = input("Introduce tu e-mail: ") #El usuario ingresa una direccion de correo

for i in range (len(email)): #Bluque for que utiliza como rango la longitud del mail introducido
	if email[i]=="@": #Verificacion de la presencia de la letra @
		valido = True

if valido == True:
	print("E-mail correcto")
else:
	print("E-mail incorrecto")