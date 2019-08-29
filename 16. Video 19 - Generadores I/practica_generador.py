def generaPares(limite): #Defino una funcion con 1 argumento que sera utilizado como limite de la cantidad de elementos en la lista

	num = 1 #Creo una variable con valor inicial

	milista = [] #Creo una lista vacia

	while num<limite: #Bucle while

		milista.append(num*2)

		num = num+1

	return(milista) #Retorna la lista

print(generaPares(10)) #Ejemplo de uso de la funcion generaPares