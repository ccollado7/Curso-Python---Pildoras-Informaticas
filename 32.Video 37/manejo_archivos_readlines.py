#Importo el modulo
from io import open

#Abro un archivo en modo lectura
archivo_texto = open("archivo.txt","r")

#Almaceno en una lista lo que leo del archivo
lineas_texto = archivo_texto.readlines()

#Cierro el archivo
archivo_texto.close()

print(lineas_texto) #Cada linea de texto es un elemento de la lista

print(lineas_texto[0])
print(lineas_texto[1])

