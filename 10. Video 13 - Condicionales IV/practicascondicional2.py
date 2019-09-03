#Utilizo la sentencia lower() para el string de forma tal de no tener case sensitive en la intrduccion de la materia

print("Asignatura optativas Año 2019 - Segundo Semestre")
print("Asiganaturas Optativas: Informatica Grafica - Pruebas de Software - Usabilidad y accesibilidad")
opcion_asignatura = input("Escribe la asignatura elegida:")

asignaturas = opcion_asignatura.lower()

#Uso del operador in para ver si un string (en este caso una asignatura) se encuentra incluido en una lista predefinida

if asignaturas in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
	print("Asiganatura elegida" + asignaturas)
else:
	print("La asignatura escogida no  esta contemplada en el Plan de Estudio")
