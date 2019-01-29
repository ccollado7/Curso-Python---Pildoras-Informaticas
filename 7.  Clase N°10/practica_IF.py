def evaluacion(nota): #Defino una funcion que recibe como parametro una nota
	valoracion="aprobado" #Creo una variable denominada valoracion
	if nota<5: #Condicional IF. Al final se tienen que especificar los : que es donde termina la condicion
		valoracion="suspenso" #Se especifica que si la nota es menor que 5 tiene que cambiar la variable valoracion aprobado a suspenso. Importante la sangria que permite aclarar que forma parte del condicional IF
	return valoracion #Devuelve lo almacenado en la variable valoracion
print(evaluacion(6)) #Defino el valor 4 para que se ejecute el programa

