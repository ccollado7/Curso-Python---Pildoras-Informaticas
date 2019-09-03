print("Asignatura optativas Año 2019 - Segundo Semestre")
print("Asiganaturas Optativas: Informatica Grafica - Pruebas de Software - Usabilidad y accesibilidad")
asignaturas = input("Escribe la asignatura elegida:")

#Uso del operador in para ver si un string (en este caso una asignatura) se encuentra incluido en una lista predefinida

if asignaturas in ("Informatica Grafica","Pruebas de Software","Usabilidad y accesibilidad"):
	print("Asiganatura elegida" + asignaturas)
else:
	print("La asignatura escogida no  esta contemplada en el Plan de Estudio")



