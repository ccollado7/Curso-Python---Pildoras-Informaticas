#Importo el modulo
from io import open

#Abro el archivo en modo lectura
archivo_texto = open("archivo.txt","r")

archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())
