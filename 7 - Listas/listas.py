#Listas
#Sintaxis
#lista = [] #Lista vacia
#Las listas comienzan con el indice 0
#print(lista) #Mostrar una lista
#Podemos almacenar diferentes tipos de datos
lista = ["Lunes", "Martes", "Miercoles", "Juevez", "Viernes", "Miercoles", 40, 40, 40, 5.67, [1, 2 , 3], True, "Lunes"]
#print(lista)
#print(lista[0])#Mostrar un elemento[]
#print(lista[-1])#Mostrar un elemento del final al principio
#print(lista[0:3])#Podemos imprimir un rango de elementos, y este llegara siempre uno antes y de igual forma si no le indicamos el inicio python lo toma que iniciamos desade 0 [0:4]
#o sino le indicamos el final pasara lo mismo [1:], pensara que es el final

#el metodo len retorna el tamaño de la lista
    #print(len(lista))

#la funcion count nos permite saber cuantas veces se encuentra un elemento en la lista
    #print(lista.count(40))

#el metodo clear nos elimina todos los elementos de la lista
    #lista.clear()

#el metodo reverse nos permite voltear los valores de la lista
    #lista.reverse()

#el metodo sort nos permite ordenar los elementos de una lista en forma ascendente
    # #lista = [1, -5, 4, 6, 3 ]
    #lista.sort()
    #print(lista)

#el metodo sort(reverse=True) nos permite ordenar los elementos de una lista en forma descendente
    # #lista = [1, -5, 4, 6, 3 ]
    # lista.sort(reverse=True)
    # print(lista)