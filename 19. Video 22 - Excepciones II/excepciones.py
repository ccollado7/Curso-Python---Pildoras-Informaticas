def suma(num1,num2):
	return(num1 + num2)

def resta(num1,num2):
	return(num1 - num2)

def multiplica(num1,num2):
	return(num1 * num2)

def divide (num1,num2):
	try: #Se indica que se "intente" realizar esta operacion. En caso que no lo consiga ejecutara lo que se encuentre dentro del bloque except
		return(num1/num2)

	except ZeroDivisionError: #Bloque de codigo que se ejecutara en caso que falla el bloque try. Importante la especificacion del tipo de error
		print("No se puede dividir entre cero")
		return("Operacion erronea")

try: #Bloque try para capturar otro tipo de error
	op1 = int(input("Introduce el primer numero: "))
	op2 = int(input("Introduce el segundo numero: "))

except ValueError: #Bloque except correspondiente a try
	print("Los valores introducidos no son correctos")

operacion = str(input("Introduce la operacion a realizar(suma,resta,multiplica,divide: "))

if operacion == "suma":
	print(suma(op1,op2))

elif operacion == "resta":
	print(resta(op1,op2))

elif operacion == "multiplica":
	print(multiplica(op1,op2))

elif operacion == "divide":
	print(divide(op1,op2))

else:
	print("Operacion seleccionada no contemplada en el programa")

print("Operacion ejecutada. Continuacion de ejecucion del Programa")

