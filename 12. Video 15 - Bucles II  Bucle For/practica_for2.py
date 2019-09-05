email = False #Inicializo la variable email on un valor False

for i in "juan@pildorasinformaticas.es": #Creo el bucle for de forma tal de recorrer todos los caracteres del e-mail
	if(i=="@"): #Verifico si el e-mail tiene la letra @, la cual considero como condicion necesaria para que la direccion de mail sea correcta.
		email== True #Si el condiciones es correcto modifico la variable e-mail a True
if email == True: #Si se encontro la letra @ entonces se ejecuta esta porcion de codigo
	print("El e-mail es correcto")

else: #Si no se encontro la letra @ entonces se ejecuta esta porcion de codigo
	print("El e-mail es incorrecto")