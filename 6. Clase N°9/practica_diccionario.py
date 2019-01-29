midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"} #Creacion de un diccionario

print(midiccionario["Francia"]) #Imprimir una referencia del diccionario indicando la clave

print(midiccionario) #Impresion del diccionario completo

midiccionario["Italia"]="Lisboa" #Genero una clave errornea para despues corregir
print(midiccionario)

midiccionario["Italia"]="Roma" #Genero una nueva clave para que se sobrescriba. En un diccionario no pueden existir 2 claves iguales
print(midiccionario)

del midiccionario["Reino Unido"] #Como se eliminan elementos del diccionario
print(midiccionario)

midiccionario1={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3} #Como crear un diccionario con diferentes tipos de datos
print(midiccionario1)

mitupla=("España","Francia","Reino Unido", "Alemania") #Defino una tupla para luego ser utilizada por un diccionario. Utilizo una tupla para asignar los valores a las clases
midiccionario2={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(midiccionario2)

print(midiccionario2["Francia"]) #Ante el pedido de una clave se entrega un valor

midiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998]} #Diccionario almacenando en su interior una tupla junto con otros valores
print(midiccionario3)
print(midiccionario3["Equipo"]) #Accedo a la clave "Equipo" 
print(midiccionario3["Anillos"]) #Acceso a la clave "Anillos" 

midiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}} #La clave la convierto en un diccionario de forma tal que quede dentro del diccionario original
print(midiccionario4["Anillos"])
print(midiccionario4)

print(midiccionario4.keys()) #Utilizo el metodo keys que devuelve las claves del desarrollo

print(midiccionario4.values()) #Utilizo el metodo values que devuelve los valores

print(len(midiccionario4)) #Utilizo len que devuelve la longitud del diccionario









