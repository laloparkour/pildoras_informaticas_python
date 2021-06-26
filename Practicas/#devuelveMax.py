n_uno = int(input("Ingresa el num #1: "))
n_dos = int(input("Ingresa el num #2: "))

def DevuelveMax(n_uno, n_dos):
	if n_uno > n_dos:
		print("El mayor es el num #", n_uno)
	elif n_dos > n_uno:
		print("El mayor es el num #", n_dos)
	else:
		print("Los numeros son iguales")

DevuelveMax(n_uno, n_dos)