class vehiculos():
	def __init__(self,marca,modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = True

	def arrancar(self):
		self.enmarcha = True

	def acelera (self):
		self.acelera = True

	def frenar (self):
		self.frenar = True

	def estado(self):
		print("Marca: ", self.marca, "\n Modelo: ", self.modelo, 
			"\n En marcha : ", self.enmarcha, "\n Acelerando: ", self.acelera,
			"\n Frenando: ", self.frena )

#Creamos una clase que hereda las propiedades y metodos de la clase vehiculos()

class Moto(vehiculos):
	pass

miMoto = Moto("Honda","CBR") #Tengo que pasar marca y modelo para el constructor de la clase vehiculo()

miMoto.estado()