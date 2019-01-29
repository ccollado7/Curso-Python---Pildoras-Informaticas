print("Verificacion de acceso")
nota_alumno=int(input("Introduce tu nota, por favor:"))
if nota_alumno<5:
	print("Insuficiente")

elif nota_alumno<6:
	print("Suficiente")

elif nota_alumno<7:
	print("Bien")

elif nota_alumno<9:
	print("Notable")

else:
	print("Sobresaliente")

#Al colocar elif se logra que toda la estructura trabaje como un solo bloque. El else se ejecuta cuando no ha entrado en ninguno de los otros
