"""Que son las expresiones regulares? son una especie de minilenguaje de programacion dentro de otro
lenguaje de programacion, son una secuencia de caracteres que forman un patrón de búsqueda.

Para que sirven? para el trabajo y el procesamiento de texto.
Ejemplo: buscar un textgo que se ajusta a un formato determinado (correo electronico)
Buscar si existe o no una cadena de caracteres dentro de un texto.
Contar el número de coincidencias dentro de un texto. """

#importar modulo re
import re

cadena = "Vamor a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla."
#metodo search(): nos permite hacer una busqueda de un string y localizarlo
#primer parametro es la palabra que deseamos buscar y el segundo es la variable
#Este nos devuelve un objeto si esta y none si no esta
#print(re.search("aprender", cadena))

textoBuscar = "Python"
"""if re.search(textoBuscar, cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")"""

#metodo start(): este nos dice el numero del caracter donde comienza a encontrar el texto
textoEncontrado = re.search(textoBuscar, cadena)
print(textoEncontrado.start())

#metodo end(): este nos dice el numero del caracter donde termina el texto a buscar
print(textoEncontrado.end())

#metodo span(): nos devuelve en una tupla la posicion del cartacter donde comienza a encontrar el texto
#y finaliza el texto encontrado
print(textoEncontrado.end())

#metodo findall(): encuentra todas las coincidencias del texto a buscar en una frase y nos lo devuelve en una lista.
print(re.findall(textoBuscar, cadena))
#Imprimir la longuitud de la lista de la palabra a buscar o las veces que encuentra la palabra
print(len(re.findall(textoBuscar, cadena)))

