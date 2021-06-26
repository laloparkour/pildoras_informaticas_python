contra = input("Introduce una contraseña: ")
c = 0

for i in range(len(contra)):
	if contra[i] == " ":
		c = 1

if len(contra) < 8 or c > 0:
	print("Contraseña errónea")
else:
	print("Contraseña correcta")
