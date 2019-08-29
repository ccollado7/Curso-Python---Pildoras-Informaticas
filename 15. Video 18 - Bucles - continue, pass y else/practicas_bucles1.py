nombre = "Pildoras Informaticas" #Defino la variable nombre y contiene un string
print(len(nombre)) #Cuento la cantidad de caracteres. El espacio en blanco tambien se cuenta

# A continuacion utilizando el bucle for cuanto la cantidad de caracteres de la variable nombre. Da igual resultado que utilizar len()
contador = 0

for i in nombre:
	contador +=1 #Incremento en 1 el valor de contador
print(contador)


#Modifico el codigo con un condicional if de forma tal de evitar contar el espacio en blanco
contador1 = 0
for i in nombre: #Declaro el bucle
	if i==" ": #Si encuentra un espacio en blanco se ignora la linea de codigo contador +=1. Por lo tando no se cuenta como caracter
		continue
	contador1 +=1
print(contador1)