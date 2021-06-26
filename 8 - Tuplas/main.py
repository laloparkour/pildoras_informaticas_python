# para convertir una tupla en un arreglo utilizamos el metodo list
# sintaxis arreglo=list(trupla a convertir)
# pruebaTupla = ("Isaac", 26, 9, 1992)
# pruebaArreglo=list(pruebaTupla)
# print(pruebaArreglo)

# para convertir un arreglo en tupla utilizamos el metodo tuple
# sintaxis 
# miArreglo = ["Isaac", 26, 9, 1992, "Isaac"]
# miTupla=tuple(miArreglo)
# print(miTupla)
# con la funcion in nos permite comprobar si hay un elemento en la tupla
# print("Isaac" in miTupla)
# el metodo count nos permite averiguar cuantos veces se encuentra un elemento dentro de una tupla
# print(miTupla.count("Isaac"))
# el metodo len nos permite saber la longitud de una tupla
# print(len(miTupla))
# para crear una tupla unitaria la tupla debe contener un elemento con una coma seguida del elemento
# miTupla=("Isaac",)
# print(len(miTupla))
# escribir una tupla sin parentesis se le conoce como empaquetado de tupla
# miTupla="Isaac", 26, 9, 1992
# el desempaquetado de una tupla nos permite asignar todos los elementos que conforman una tupla en
# variables
miTupla=("Isaac", 26, 9, 1992)
nombre, dia, mes, agno = miTupla
print(nombre)
print(dia)
print(mes)
print(agno)
# no podemos utilizar nada que modifique una tupla, como son las funciones o metodos que utilizamos
# en los arreglos
