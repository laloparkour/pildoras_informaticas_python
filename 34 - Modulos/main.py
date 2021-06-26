#Un modulo es un archivo con extension .py, .pyc(python compilado) o archivo escrito en C para CPython
#La utilizad de los modulos es organizar y reutilizar nuestro codigo(modularizacion y reutilizacion)
#Modularizacion: dividir el codigo en pequeñas partes

#Para utilizar un modulo en python debemos importarlo y para ello utilizamos
#la instruccion o directiva import
#Ejemplo: import nombre_modulo

#import funciones_matematicas
#Para no tener que anteponer el nombre del modulo en cada funcion utilizamos from
#Ejemplo: from nombre_modulo import funcion o (*, nos permite utilizar todas las funciones disponibles)
#Ejemplo: from funciones matematicas import sumar
from funciones_matematicas import *

#para utilizar las funciones de un modulo usamos la nomenclatura del punto
#Ejemplo: nombre_modulo.funcion()
#funciones_matematicas.sumar(5,5)
#funciones_matematicas.restar(5,2)

sumar(5, 4)
restar(5,1)


