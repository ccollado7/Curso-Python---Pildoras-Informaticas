#Programa que pregunta la edad. El valor correcto debe estar comprendido entre 6 y 99 años

edad = int(input("Introduce tu edad por favor: "))

while edad<5 and edad>100:
	print("Se introdujo una edad negativa, vuelve a intentarlo:")
	edad = int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar")
print("Tu edad es: " + str(edad))