#Una funcion lambda es una funcion anonima y se utilizan en python para abreviar, para que la sintaxis
#sea mas ligera y nos ahorremos tiempo, consiste en resumir una funcion normal en una exprecion LAMBDA
#todo lo que podemoshacer con una exprecion lambda se puede hacer con una funcion normal pero no alrrevez

#Realizar repetidamente el calculo de el area de un triangulo
"""def area_triangulo(base, altura):
    return (base*altura)/2

triangulo1 = area_triangulo(5, 7)
triangulo2 = area_triangulo(9, 6)

print(triangulo1)
print(triangulo2)"""
#Uso de una funcion lambda
#Se llama funcion anonima por que no tienen nombre, tambien se les denomnia funciones on the go, on demand o online
#son terminos para denominarlas como funciones rapidas
#una funcion esta nunca podra tener condicionales ni bucles, esta diseñada para funciones sencillas
#en una funcion lambda despues de escribir los parametros que vamos a utilizar, se ponen (:- dos puntos)
#como si hubieramos puesto un return
area_Triangulo = lambda base, altura:(base*altura)/2
print(area_Triangulo(7, 5))
print(area_Triangulo(5, 10))

al_Cubo = lambda numero:pow(numero, 3)
al_Cubo = lambda numero:numero**3
print(al_Cubo(5))

destacar_valor = lambda comision:"¡{}! $".format(comision)

comision_Ana = 15585
print(destacar_valor(comision_Ana))