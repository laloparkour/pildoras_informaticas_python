# estructuras de flujo
# flujo de ejecuccion de un programa: es el orden con el que se ejecutan
# sus instrucciones

#sintaxis

print("Programa de evaluación de notas de alumnos")
nota_alumno = int(input("Ingresa una nota: "))

def evaluacion(nota):
	valoracion="aprobado"
	if nota <= 5:
		valoracion="reprobados"
	return valoracion

print(evaluacion(nota_alumno))


edad = int(input("Ingresa tu edad: "))

if edad < 18:
	print("No puedes pasar")
elif edad > 100:
	print("Edad incorrecta")
else:
	print("Puede pasar")