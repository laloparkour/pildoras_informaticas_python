num = int(input("Introduce un número: "))
suma = 0

while num > 0:
	suma = suma + num
	num = int(input("Introduce otro número: "))

print("La suma de los numeros introducidos es", suma)