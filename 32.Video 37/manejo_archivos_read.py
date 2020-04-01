#Importo el modulo
from io import open

#Abro un archivo en modo lectura
archivo_texto = open("archivo.txt","r")

#Almaceno en esta variable lo que leo del archivo
texto = archivo_texto.read()

#Cierro el archivo
archivo_texto.close()

print(texto)