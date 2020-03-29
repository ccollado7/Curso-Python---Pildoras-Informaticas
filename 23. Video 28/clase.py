class Coche():
	
	
	def __init__(self):
		self.__larcoChasis = 250 
		self.__anchoChasis = 120 
		self.__ruedas = 4 
		self.__enmarcha = False

	def arrancar(self,arracamos):
		self.__enmarcha = arracamos

		if (self.__enmarcha):
			chequeo = self.__chequeo_interno() 

		if (self.__enmarcha and chequeo):
			return ("El coche esta en Marcha")
		elif (self.__enmarcha and chequeo == False):
			return ("Algo ha ido mal en el chequeo, no podemos arrancar")
		else:
			return("El coche esta parado")


	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ",self.__anchoChasis, " y un largo de ", self.__larcoChasis)

	def __chequeo_interno(self):
		print("Realizando chequeo interno")
		self.gasolina = "Ok"
		self.aceite = "Ok"
		self.puertas = "Cerrada"

		if self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerrada":
			return True
		else:
			return False

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()


print("----------A continuacion creamos el segungo objeto -------")

miCoche2 = Coche()
print(miCoche.arrancar(False))
miCoche2.estado()
