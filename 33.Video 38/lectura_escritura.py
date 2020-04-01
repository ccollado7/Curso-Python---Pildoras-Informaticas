#Importo el modulo
from io import open

#Abro el archivo en modo lectura y escritura
archivo_texto = open("archivo.txt","r+")

#Por defecto al abrir el archivo el puntero estara en la posicion 0
archivo_texto.write("Comienzo del texto")
