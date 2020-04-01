#Importo el modulo
from io import open

#Abro el archivo en modo lectura
archivo_texto = open("archivo.txt","r")

#Situo el cursor en la mitad del texto
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())
