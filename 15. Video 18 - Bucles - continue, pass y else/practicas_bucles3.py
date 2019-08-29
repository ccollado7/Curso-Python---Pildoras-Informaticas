email = input("Introduce tu e-mail por favor: ")

for i in email:
	if i=="@": #Busco si existe la palabra @
		arroba=True
		break #En la ejecucion del bucle for apenas se encuentre una @ el programa saldra del bucle for y continuara la ejecuion mas adelante

else: #Este else no forma parte del if declarado dentro del for. La sentencia else declarada en este lugar se ejecutara cuando el bucle for se recorra completamente o se ejecute la sentencia break
	arroba = False

print(arroba)
