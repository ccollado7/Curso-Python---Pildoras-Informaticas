edad = input("Introduce la edad: ")

while (edad.isdigit() == False):
	print("Por favor Introduce un valor numerico")

	edad = input("Introduce la edad: ")

if(int(edad) <18):
	print("No puede pasar")
else:
	print("Puede pasar")