def divide():
	
	try:

		op1 = float(input("Introduce el primer numero: "))
		op2 = float(input("Introduce el segundo numero: "))

		print("La division es: " + str(op1/op2))

	except ValueError: #Primera excepcion
		print("El valor introducido es erroneo")

	except ZeroDivisionError: #Segunda excepcion
		print("No se puede dividir entre 0!")

	finally: #Cuando quiere que una linea de codigo se ejecute siempre lo coloco dentro de una clausula finally. Esta se ejecuta ocurra o no un error.

		print("Calculo finalizado")

divide()