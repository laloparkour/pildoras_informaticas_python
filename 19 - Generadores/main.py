#Son extructuras que extraen valores de una función
#y se almacenan en objetos iterables(que se pueden recorrer).
#Estos valores se almacenan de uno en uno
#Cada vez que un generador almacena un valor, este permanece en un estado
#de pausado hasta que se solicita el siguiente.
#Esta caracteristica es conocida como suspensión de estado(stand by).
#Este estado de suspencion hace que se ahorren recursos

#sintaxis
#def nombre_funcion():
	#instruccion

	#yield resultato (construye un objeto iterable con el primer valor)

#Ventajas de obtener valores de uno en uno
#Son más eficientes que las funciones tradicionales.
#Muy útiles con listas de valores infinitos.
#Bajo determinados escenarios, será muy útil que un generador devuelva
#los valores de uno en uno.

#crear un programa que nos genere una lista de numeros pares
#funcion tradicional
# def numeros(limite):
# 	num = 1
# 	miArreglo = []

# 	while num < limite:
# 		miArreglo.append(num*2)
# 		num += 1
# 	return miArreglo

# print(numeros(10))

# #funcion con generadores
# def numeros(limite):
# 	num = 1

# 	while num < limite:
# 		yield num * 2
# 		num += 1
# devuelvePares = numeros(10)

# #El metodo next nos devuelve el primer valor que tiene almacenado
# #un generador en su interior.
# print(next(devuelvePares))
# print("Aqui podría ir más código...")
# print(next(devuelvePares))
# print("Aqui podría ir más código...")
# print(next(devuelvePares))
# print("Aqui podría ir más código...")

#yield from nos permite simplificar código de los generadores en el caso
#de utilizar bucles anidados dentro del generador.

#Cuando ponemos un asterisco antes de un argumento estamos diciendo que 
#va a recivir un numero indeterminado de elementos, y ademas los va a
#recivir en forma de tupla.
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		# for subElemento in elemento:
			yield from elemento #

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

