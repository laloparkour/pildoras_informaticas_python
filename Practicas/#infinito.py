n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

while n2 > n1:
	n1 = n2
	n2 = int(input("Ingresa un segundo numero: "))

print(n2, "no es mayor que", n1) 