email = input("Introduce un correo: ")

i = 0
a = 0
b = 0
for i in range(len(email)):
	if email[i] == "@":
		a += 1
	if email[i] == ".":
		b += 1
if a != 1 or b == 0:
	print("El correo es incorrecto")
else:
	print("El correo es correcto")