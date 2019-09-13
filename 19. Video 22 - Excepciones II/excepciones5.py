def divide():
	
	try: #Ejecucion del bloque try

		op1 = float(input("Introduce el primer numero: "))
		op2 = float(input("Introduce el segundo numero: "))

		print("La division es: " + str(op1/op2))

	#No utilizo las clausulas except

	finally: #En caso de un error el programa no captura nada pero por lo menos no se cae y se ejecuta lo que se encuentra dentro del bloque finally

		print("Calculo finalizado")

divide()