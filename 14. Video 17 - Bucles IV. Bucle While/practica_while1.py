#Programa que pregunta la edad. Si la edad es negativa vuelve a preguntar hasta que se introduce un valor positivo

edad = int(input("Introduce tu edad por favor: "))

while edad<0:
	print("Se introdujo una edad negativa, vuelve a intentarlo:")
	edad = int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar")
print("Tu edad es: " + str(edad))
