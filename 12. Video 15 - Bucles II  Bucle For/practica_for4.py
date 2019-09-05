#Evaluo la validez de un e-mail por la presencia de la letra @ y el punto .


contador = 0 #Inicializo una variable denominada contador

email = False #Inicializo la variable email con un valor False

mi_Email = str(input("Introduce tu direccion de e-mail: ")) #Almaceno el mail en esta variable

for i in mi_Email: #Creo el bucle for de forma tal de recorrer todos los caracteres del e-mail
	if(i=="@" or i=="."):
		
		contador = contador +1


if contador == 2: #Si se encontro la letra @ entonces se ejecuta esta porcion de codigo
	print("El e-mail es correcto")

else: #Si no se encontro la letra @ entonces se ejecuta esta porcion de codigo
	print("El e-mail es incorrecto")