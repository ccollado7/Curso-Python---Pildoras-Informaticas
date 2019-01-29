salario_presidente=int(input("Introduce el salario del presidente:"))
print("Salario Presidente:"+str(salario_presidente)) #Python al ser FUERTEMENTE TIPADO, lo cual significa que hace una distincion fuerte entre distintos tipos de datos. No es posible concatenar una valor de tipo STRING con un valor del tipo INTEGER (entero/int)

salario_director=int(input("Introduce el salario del Director:"))
print("Salario Director:"+str(salario_director))

salario_jefe_area=int(input("Introduce el salario del Jefe de Area:"))
print("Salario Jefe de Area:"+str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del Administrativo:"))
print("Salario Administrativo:"+str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("No se produce solapamiento salarial")
else:
	print("Se produce solapamiento salarial y se tiene que corregir!")



#La funcion STR convierte lo que este dentro de sus parentesis en un string. De esta forma lo puedo concatenar con el string que necesite para armar una oracion compuesta