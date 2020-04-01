#Importo el modulo
from io import open

#Abro el archivo para agregar otras lineas
archivo_texto = open("archivo.txt","a")

#Escribo una nueva linea sobre el archivo abierto
archivo_texto.write("\n siempre es una buena ocacion para estudiar Python")

#Cierro el archivo
archivo_texto.close()
