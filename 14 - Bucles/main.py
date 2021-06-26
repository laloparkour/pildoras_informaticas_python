# la utilidad del bucle es repetir una o varias lineas de codigo varias veces
#sintaxis
# for variable in elemento a recorrer:
# 	cuerpo del bucle o elementos

# for i in [1,2,3]:
# 	print("Hola")

# for x in ["Primavera","Verano","Otoño","Invierno"]:
# 	print(x)

# for i in ["pildoras", "informaticas", 10]:
	# print("hola", end=" ")
	
# en python True and False van con la primera letra en mayuscula
# if email == True: se puede escribir if email: cuando queramos
# comprobar si la variable es igual a true
# (=) se utiliza para asignar y (==) se utiliza para comparar
# contador=0
# email = (input("Ingresa un correo: "))
# for i in email:
# 	if i=="@" or i==".":
# 		contador = contador + 1

# if contador == 2:
# 	print("El email es correcto")
# else:
# 	print("El email es incorrecto")

# (valor_inicio, hasta donde menos uno, de cuanto en cuanto)
# for i in range(5,50,3):
# 	print(f"valor de la variable {i}")

# valido = False

# email = input("Introduce tu email: ")

# for i in range(len(email)):
# 	if email[i] == "@":
# 		valido = True
# if valido:
# 	print("Email correcto")
# else:
# 	print("Email incorrecto")

# el bucle while es un bucle indeterminado por que no sabemos cuantas
# veces se ejecutara el codigo en su interior
#sintaxis
# while condicion:
	#cuerpo del bucle

# i = 1
# while i<=10:
# 	print("Ejecucion ", i)
# 	i=i+1
# print("Termino de la ejecución")

# edad = int(input("Introduce tu edad: "))

# while edad < 5 or edad > 100:
# 	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
# 	edad = int(input("Introduce tu edad: "))

# print("Gracias por colaborar. Puedes pasar")
# print("Edad de el aspirante ", edad)

# import math
# print("Programa de calculo de raiz cuadrada")
# num = int(input("Introduce un número: "))

# intentos = 0

# while num < 0:
# 	print("No se puede hallar la raíz de un número negativo")

# 	if intentos == 2:
# 		print("Intentos máximos excedidos")
# 		break;

# 	num = int(input("Introduce un número: "))
# 	if num < 0:
# 		intentos = intentos + 1

# if intentos < 2:
# 	solucion=math.sqrt(num)
# 	print("La raiz cuadrada de: ", num, "es ", solucion)

# la instruccion continue nos permite ignorar una linea o una instruccion
# for letra in "Python":
# 	if letra == "h":
# 		continue 
# 	print("viendo la letra: ", letra)

# nombre = "Pildoras Informaticas"

# contador = 0

# for i in nombre:
# 	if i == " ":
# 		continue
# 	contador += 1
# 	# (contador = contador + 1) es lo mismo que (contador += 1) 
# print(contador)

# # la instruccion pass nos permite dejar algun ciclo, funcion, clace, etc
# # para despues trabajar con el
# class MiClase:
# 	pass # para implementar mas tarde 

# la instruccion else se ejecuta cuando se haya recorrido el for y el ciclo
# no cumpla la condicion o la instruccion
email = input("Introduce tu email: ")

for i in email:
	if i == "@":
		arroba = True

		break;
else:
	arroba = False

print(arroba)
