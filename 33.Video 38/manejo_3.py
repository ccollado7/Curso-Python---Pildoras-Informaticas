#Importo el modulo
from io import open

#Abro el archivo en modo lectura y escritura
archivo_texto = open("archivo.txt","r+")

#Devuelve una lista con las lineas del archivo
print(archivo_texto.readlines())
