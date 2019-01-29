print("Programa de evaluacion de notas de alumnos") #Defino un titulo
nota_alummno=input("Introduce la nota del alumno:") #El programa se detiene y queda a la espera que se introduzca un valor por teclado
def evaluacion(nota): #Defino el condicional de nuevo
	valoracion="Aprobado"
	if nota<5:
		valoracion="Suspenso"
	return valoracion
print(evaluacion(int(nota_alummno))) #Utilizo la funcion INT transformara en entero (siempre que sea posible) lo que se introduzca

#Flujo de ejecucion del programa:
	#Se ejecuta la primer linea con el mensaje
	#Se ejecuta la segunda linea quedando el programa a la espera que se introduzca la nota por teclado
	#El dato introducido se almacane an nota_alumno
	#El programa continuaria con la ejecucion. La funcion evaluacion es llamada dentro del PRINT y se ejecutara la funcion evaluacion
	#Lo que esta almacenado en la variable nota-alumno "viaja" y se almacena en la variable "nota"

#Para que sublime permita introducir informacion por teclado se tiene que abrir la consola
#El valor introducido por teclado es considerado como texto. Cualquier cosa que se introduzca por medio de la funcion input es considerado como TEXTO, por lo tanto el 7 es considerado texto. El programa da error por que no se puede comparar un texto con un numero
#Utilizo la funcion INT transformara en entero (siempre que sea posible) lo que se introduzca
#La funcion INPUT puede admitir parametros (ej: incluir un mensaje)
#Cuando trabajamos con IF y con funciones tenemos que tener en cuenta el AMBITO: Una variable solamente es accesible dentro de un ambito
	#Ejemplo: La variable "valoracion" fue declarado dentro de una funcion (tener en claro donde comienza y donde termina). Fuera de ese ambito la vaiable NO SE PUEDE manipular o leer
	#Si dentro del IF declaro otra variable "calificacion" esta variable solo es accesible dentro del ambito del bloque IF
	