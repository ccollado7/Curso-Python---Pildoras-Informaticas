print("Verificacion de acceso")
edad_usuario=int(input("Introduce tu edad por favor:"))
if edad_usuario<18:
	print("No puedes pasar")
else:
	print("Puedes pasar") #Else se puede traducir como "y si no es verdad". Cada ELSE tiene que ir acompañado de un IF
print("El programa ha finalizado")

#El ELSE trabaja  con el IF mas cercano, asi que tener cuidado como lo colocamos