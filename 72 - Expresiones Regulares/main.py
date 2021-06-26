#Funcion match(): busca si hay coincidencias en un patron de busquedas al comienzo de una cadena de texto
#Funcion search():
#La diferencia entre estas dos funciones es que la funcion match busca al principio de una cadena de texto
#la funcion search busca en toda la cadena de texto si el patron de busqueda se encuentra o no
import re

nombre1 = "Jara López"
nombre2 = "Antonio Gómez"
nombre3 = "Lara López"

codigo1 = "jkjlasfkasjfkasjfkajsfs71asdasdlasdlas"
codigo2 = "asdasjdasoasopdiasdas71asdasdqweqwasqwas"
codigo3 = "asdasdasdasd asd asdasd asd asdasd"

#La funcion match admite un tercer parametro al que se denomina flag
#Nos permite que la funcion no sea sencible a mayusculas y minisculas(deshabilitar el key sencitive)
#if re.match("Sandra", nombre3, re.IGNORECASE):
#El comodin punto nos permite buscar por una letra sin determinar seguido de la cadena de caracteres
#if re.match(".ara", nombre1, re.IGNORECASE):
#La expresion regular \d nos permite buscar si en la cadena que estamos buscando el patron de busqueda
#comienza por un numero o no comienza por un numero
#if re.search("López", nombre3):
if re.search("71", codigo1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")