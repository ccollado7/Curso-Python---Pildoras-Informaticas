class Coche():
	
	#Estado inicial de todos los objetos (constructor)
	def __init__(self):
		self.larcoChasis = 250
		self.anchoChasis = 120
		self.__ruedas = 4 #Encapsulo esta variable para que no sea accesible desde fuera de la clase
		self.__enmarcha = False #Encapsulo la variable

	#Primer metodo -  Me permite cambiar el estado de un objeto y arrancarlo
	def arrancar(self,arracamos):
		self.__enmarcha = arracamos
		if (self.__enmarcha):
			return ("El coche esta en Marcha")
		else:
			return("El coche esta parado")

	#Segundo metodo - Estado general
	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ",self.anchoChasis, " y un largo de ", self.larcoChasis)



miCoche = Coche() #Estoy instanciando la clase Coche()

print(miCoche.arrancar(True)) #Arranco el coche
miCoche.estado() #Verifico el estado del coche

print("----------A continuacion creamos el segungo objeto -------")

miCoche2 = Coche() #Estoy instanciando la clase Coche()

print(miCoche.arrancar(False)) #No no arranco el coche

miCoche2.__ruedas = 2 #Intento cambiar esta variable y no puedo, la misma esta encapsulada

miCoche2.estado() #Verifico el estado del coche