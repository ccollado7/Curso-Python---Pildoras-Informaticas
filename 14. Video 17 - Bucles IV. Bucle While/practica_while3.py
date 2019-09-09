#Programa para calcular la raiz cuadrada de un numero

import math

print("Programa de Calculo de Raiz Cuadrada")

numero = int(input("Introduce el numero al cual se le calculara la raiz cuadrada: "))

intentos = 0 #Variable de inicio

while numero<0: #TEl ingreso al bucle se ejecuta si el usuario introduce un numero negativo
	print("No se puede hallar la raiz cuadrada de un numero negativo")

	if intentos == 2:
		print("Has consumidos demasiados intentos. El programa ha finalizado")
		break #Si el bucle llega a la condicion de lectura del break entonces el condicional finaliza

	numero = int(input("Introduce el numero al cual se le calculara la raiz cuadrada: "))

	if numero<0:
		intentos = intentos+1

if intentos<2:
	solucion = math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) + "es" + str(solucion))

