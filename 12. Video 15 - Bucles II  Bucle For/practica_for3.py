#Evaluo la validez de un e-mail por la presencia de la letra @

email = False #Inicializo la variable email con un valor False

mi_Email = str(input("Introduce tu direccion de e-mail: ")) #Ingreso el mail a ser evaluado

for i in mi_Email: #Creo el bucle for de forma tal de recorrer todos los caracteres de la variable que almacena el e-mail introducido
	if(i=="@"): #Verifico si el e-mail tiene la letra @, la cual considero como condicion necesaria para que la direccion de mail sea correcta.
		email== True #Si el condiciones es correcto modifico la variable e-mail a True

if email == True: #Si se encontro la letra @ entonces se ejecuta esta porcion de codigo
	print("El e-mail es correcto")

else: #Si no se encontro la letra @ entonces se ejecuta esta porcion de codigo
	print("El e-mail es incorrecto")