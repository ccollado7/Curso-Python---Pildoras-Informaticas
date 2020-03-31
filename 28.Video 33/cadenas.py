#Metodos sobre cadenas:

#1. upper(): Convierte en mayuscula todas las letras del string
#2. lower(): Covierte a minusculas todas las letras del string
#3. capitalize(): Pone la primera letra en mayuscula
#4. count(): Cuenta la cantidad de veces que aparece una letra o un grupo de caracteres dentro de una frase
#5. find(): Representa el indice (posicion) en la cual aparece un caracter o grupo de caracteres
#6. isdigit(): Devuel True / False si el digito es un numero o no
#7. isalum(): Comprueba si es un alfanumerico
#8. isalpha(): Comprueba si son solo letras (los espacios no cuentan)
#9. split(): Separa las palabras por espacios
#10. strip(): Borra espacios que sobran al principio y al final
#11. replace(): Cambia una palabra o letra por otra
#14. rfind(): Igual que find() pero comenzando desde atras

nombreUsuario = input("Introduce tu nombre de usuario: ")
print("El nombre es: ", nombreUsuario.upper())

nombreUsuario = input("Introduce tu nombre de usuario: ")
print("El nombre es: ", nombreUsuario.lower())

nombreUsuario = input("Introduce tu nombre de usuario: ")
print("El nombre es: ", nombreUsuario.capitalize())