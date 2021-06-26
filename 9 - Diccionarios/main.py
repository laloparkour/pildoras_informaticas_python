# Los disccionarios nos permiten almacenar valores de diferente tipo, arreglos e incluso otros diccionarios
# la principal caracteristica es que los datos se almacenan asociados a una
# clave, de tal forma que se crea una asociacion de clave.valor para cada elemento
# los elementos almacenados no estan ordenados. El orden es indiferente
# en un diccionario no puede haber claves iguales

#sintaxis
# midiccionario = {"Mexico":"CD Mexico", "Francia":"Paris", "Reino unido":"Londres", "España":"Madrid"}
# #para agregar un elemento mas al diccionario
# midiccionario["Italia"]="Lisboa"
# print(midiccionario["Francia"])
# print(midiccionario)
# #para modificar un valor asignado a una clave
# midiccionario["Italia"]="Roma"
# #para eliminar elementos utilizamos el metodo del
# del midiccionario["Reino unido"]
# print(midiccionario)

# mostrar una tupla en un diccionario y agregarle valores
# mitupla=["España", "Francia", "Reino Unido", "Alemania"]
# midiccionario={
# mitupla[0]:"Madrid", mitupla[1]:"Paris", 
# mitupla[2]:"Londres", mitupla[3]:"Berlin"}
# print(midiccionario)
# print(midiccionario["Francia"])

# un diccionario almacene una tupla junto con otros valores del diccionario
# midiccionario={
# 23:"Jordan", "Nombre":"Michael", 
# "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
# print(midiccionario)
# print(midiccionario["anillos"])

# guardar un diccionario dentro de otro diccionario
midiccionario={
23:"Jordan", "Nombre":"Michael", 
"Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
# el metodo keys nos devuelve las claves
print(midiccionario.keys())
# el metodo values nos devuelve los valores
print(midiccionario.values())
# el metodo len nos devuelve la longuitud
print(len(midiccionario))
print(midiccionario)
