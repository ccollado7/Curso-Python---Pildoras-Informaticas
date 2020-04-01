#Importo el modulo
from io import open

#Creo un archivo en blanco
archivo_texto = open("archivo.txt","w")

frase = "Estupendo dia para estudiar Python \n el miercoles"

#Escribo sobre el archivo una frase
archivo_texto.write(frase)

#Cierro el archivo (abierto desde memoria)
archivo_texto.close()

