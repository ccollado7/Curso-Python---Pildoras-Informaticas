class Coche():
	#Un objeto tiene un estado, propiedades y comportamiento

	#Defino las propiedades de la clase Coche()

	larcoChasis = 250 #Propiedad 1
	anchoChasis = 120 #Propiedad 2
	ruedas = 4 #Propiedad 3
	enmarcha = False #Propiedad 4

	#Defino los comportamientos la clase Coche(). Para esto defino los metodos de la clase

	
	#Primer metodo -  Me permite cambiar el estado de un objeto y arrancarlo
	def arrancar(self):
		self.enmarcha = True


	#Segundo metodo - Me permite verificar el estado del objeto ¿Esta arrancado o no?
	def estado(self):
		if (self.enmarcha == True):
			return ("El coche esta en Marcha")
		else:
			return("El coche esta parado")


#Creo un objeto o instancia de la clase Coche()

miCoche = Coche() #Estoy instanciando la clase Coche()

#¿Como puedo ver las propiedades de la instancia de clase miCoche? - Utilizo la nomenclatura del punto.

print("El largo del coche es: " , miCoche.larcoChasis)
print("El coche tiene ",miCoche.ruedas, " ruedas")

#Por medio del metodo arrancar arranco el coche
miCoche.arrancar()

#Verifico el estado del coche
print(miCoche.estado())

