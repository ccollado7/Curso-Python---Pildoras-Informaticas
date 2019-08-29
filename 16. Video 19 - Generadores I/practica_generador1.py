def generaPares(limite):

	num = 1 #Creo una variable con valor inicial

	while num<limite: #Bucle while

		yield(num*2) #Construye un objeto iterable con los valores de la lista en su interior y los va almacenando uon a uno

		num = num+1

devuelvePares = generaPares(10) #Creo una variable objeto donde almaceno el objeto iterable donde almaceno la funcion

for i in devuelvePares: #Devuelve todos los
	print(i)