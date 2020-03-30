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

#Creamos una clase furgoneta() que hereda las propiedades y metodos de la clase vehiculos()

class Furgoneta(vehiculos):
	def carga(self,cargar):
		self.cargado = cargar
		if(self.cargado):
			return("La furgoneta esta cargada")
		else:
			return("La furgoneta no esta cargada")

#Creamos una clase Moto() que hereda las propiedades y metodos de la clase vehiculos()
class Moto(vehiculos):
	hcaballito = ""

	def caballito(self): #Metodo propio de la clase Moto()
		self.hcaballito = "Voy haciendo el caballito"

	def estado(self): #Metodo que sobrescribe el el metodo estado() de la clase vechiculos()
		print("Marca: ", self.marca, "\n Modelo: ", self.modelo, 
			"\n En marcha : ", self.enmarcha, "\n Acelerando: ", self.acelera,
			"\n Frenando: ", self.frena, "\n", self.hcaballito)

#Creamos una clase vElectricos() independien, no hereda de otra clase
class vElectricos(vehiculos):
	def __init__(self,marca, modelo):
		
		super().__init__(marca,modelo)

		self.autonomia = 100

	def cargarEnergia(self):
		self.cargando = True

#Creamos una clase BicicletaElectrica() que hereda de 2 clases

class BicicletaElectrica(vElectricos,vehiculos):
	pass


miMoto = Moto("Honda","CBR") #Tengo que pasar marca y modelo para el constructor de la clase vehiculo()
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici = BicicletaElectrica("Orbea","tjh")