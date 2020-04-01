#Importo el modulo
from io import open

#Abro el archivo en modo lectura y escritura
archivo_texto = open("archivo.txt","r+")


lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()