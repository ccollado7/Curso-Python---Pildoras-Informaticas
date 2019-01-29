mi_lista=["Maria","5","True","78.35"] #Definicion de una lista
print(mi_lista[:]) #Impresion de una lista completa
print(mi_lista[2]) #Impresion del valor de la lista que tiene indice 2 de la lista
print(mi_lista[-1]) #Uso de indice negativo (comienzo desde derecha a izquierda)
print(mi_lista[0:3]) #Impresion de un intervalo de la lista
print(mi_lista[:3]) #Impresion desde el inicio de la lista hasta el item de indice 3
print(mi_lista[0:2]) 
print(mi_lista[2:])
print(mi_lista[3:])
mi_lista.append("Sandra") #Agregado de un elemento a la lista al final de la misma
print(mi_lista)
mi_lista.insert(2,"Sandra") #Agregado de un elemento a la lista en el indice 2
print(mi_lista)
mi_lista.extend(["Claudio","Guillermina","Diego"]) #Extencion de una lista
print(mi_lista)
print(mi_lista.index("Claudio")) 
mi_lista.extend(["Carlos","Claudio"])
print(mi_lista)
print(mi_lista.index("Claudio"))
print("Pepe" in mi_lista)
print("Adalberto" in mi_lista)
print(mi_lista[1])
mi_lista.remove(1)
print(mi_lista[:])









