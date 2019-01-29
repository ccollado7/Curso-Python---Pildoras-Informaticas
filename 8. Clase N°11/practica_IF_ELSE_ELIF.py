print("Verificacion de acceso")
edad_usuario=int(input("Introduce tu edad por favor:"))
if edad_usuario<18:
	print("No puedes pasar")
elif edad_usuario>100: #Al colocar elif se logra que el else no se acompañe solamente del if  mas cercano, si no que se acompaña de toda la estructura (los dos condicionales en la parte superior)
	print("Edad Incorrecta")
else: #Cuando nada de lo anterior se cumple recien en este momento se pasa al else
	print("Puedes pasar") 
print("El programa ha finalizado")