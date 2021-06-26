#Que son los paquetes? directorios o carpetas, donde se almacenarán los módulos relacionados entre si.
#Para que sirven? para organizar y reutilizar los módulos.
#Como se crean? crear una carpeta que contenga un archivo de nombre __init__.py

#Ejemplo una carpeta: from carpeta_contenedora.nombre_modulo import(funcion o *)
#from calculos.operaciones_basicas import *
#Ejemplo subcarpeta: from carpeta_contenedora.subcarpeta.modulo import(funcion o *)
from calculos.basicos.operaciones_basicas import *

sumar(5,7)