print("Programa de Becas Año 2019")

distancia_escuela = int(input("Introduce la distancia  a la escuela en kilometros:"))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el numero de hermanos en el centro:"))
print(numero_hermanos)

salario_familiar = int(input("Introduce salario anual Bruto:"))
print(salario_familiar)

#Utilizo el operador logico AND para verificar si se estan cumplieno las 3 condiciones logicas al mismo tiempo

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a Beca")
else:
	print("No tienes derecho a Besa")

#En el ejemplo anterior coloco el operador OR para darle mayor peso a la variable salario_familiar

