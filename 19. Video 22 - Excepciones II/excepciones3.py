ef divide():
	
	try:

		op1 = float(input("Introduce el primer numero: "))
		op2 = float(input("Introduce el segundo numero: "))

		print("La division es: " + str(op1/op2))

	oexcept: #Trato de capturar un error general. Da igual el error que cometa.
		print("Ha ocurrido en error")


divide()