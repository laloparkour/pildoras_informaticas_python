import random
numeros = [] #Lista de elementos generados aleatoriamente
totales = [] #Lista que te muestra cuantas veces se repite cuantos elementos
cantidad = 50  #Tamaño de la lista

#Ciclo para llenar la lista con los elementos generados aleatoriamente
for x in range(0, cantidad):
    numeros.append(random.randrange(20))

#Ciclo para recorrer la lista de elementos generados aleatoriamente
for numero in numeros:
    cont = 0
    #Ciclo para recorrer el ciclo que recorre la lista generada aleatoriamente
    for numero2 in numeros:
        #Condicional donde compara los elementos de los ciclos
        if numero == numero2:
            cont += 1
    totales.append(cont)
#Ciclo para mostrar la lista con los elementos generados aleatoriamente y las veces que se repite cada uno
for x in range(0, cantidad):
    print(numeros[x], " -", totales[x])
