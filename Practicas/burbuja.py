import random #Impor la libreria random
lista = [] #Declaramos la lista vacia
cambio = True

#Ciclo que llena la lista
for x in range(0,10,1):
    lista.append(random.randrange(20)) #Añadimos los valores a la lista con el metodo randrange de la libreria random

#Ciclo que muestra los elementos de la lista
for x in range(0,10,1):
    print(lista[x], end=" ")
print("\n")

#Metodo Burbuja
while (cambio): #Ciclo que pregunta si a habido algun cambio
    cambio = False
    for x in range(0, 10, 1):
        if (x+1 < len(lista) and lista[x] > lista[x+1]):
             cambio = True
             acum = lista[x]
             lista[x] = lista[x+1]
             lista[x+1] = acum

#Ciclo que muestra la lista ordenada
for x in range(0, 10, 1):
    print(lista[x], end=" ")