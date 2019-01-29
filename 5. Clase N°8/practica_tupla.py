mitupla=("Juan", 13,1,1995) #Definicion de tupla
print(mitupla[3])

milista=list(mitupla) #Transformacion de tupla en lista
print(milista)
print(mitupla)


milista1=["Juan", 13,1,1995] #Transformacion de lista en tupla
mitupla1=tuple(milista1)
print(mitupla1)
print(milista1)

print("Juan" in mitupla) #Verificacion si un elemento se encuentra en una tupla
print("Claudio" in mitupla)

print(mitupla.count(13)) #Contaje de elementos dentro de una tupla

mitupla2=("Juan", 13,1,1995,13)
print(mitupla2.count(13))

print(len(mitupla)) #Longitud de tupla
print(len(mitupla2))

mitupla3=("Juan",) #Definicion de tupla unitaria
print(mitupla3)
print(len(mitupla3))

mitupla4="Juan",13,1,1995 #Esta notacion puede llevar a confusion
print(mitupla4)

mitupla=("Juan", 13,1,1995) #Desempaquetado de tuplas / almacenaje de variables dentro de una tupla
nombre,dia,mes,agno=mitupla
print(nombre)
print(agno)
print(dia)
print(mes)

mitupla.append("paco") #La tupla es estatica y no permite incorporar nuevos elementos




