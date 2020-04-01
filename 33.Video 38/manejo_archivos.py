#Importo el modulo
from io import open

#Abro el archivo en modo lectura
archivo_texto = open("archivo.txt","r")

archivo_texto.seek(11) #Coloca el puntero en la posicion 11

print(archivo_texto.read()) #Las 10 primeros letras no las lee

archivo_texto.seek(0) #Vuelve el puntero a la posicion 0 (inicio del texto)

