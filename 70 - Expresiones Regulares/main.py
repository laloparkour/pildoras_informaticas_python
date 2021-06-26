#Meta caracteres: caracteres comodin
#Anclas: nos permite encontrar coincidencias de texto al inicio y al final

import re

lista_nombres = ['Ana Gómez',
                 'Maria Martin',
                 'Sandra López',
                 'Santiago Martín',
                 'Sandra Fernández']

for elemento in lista_nombres:
    #Para hacer uso de las anclas: uitiliamos los caracteres ^ al inicio de la palabra para buscar
    # los que inician y $ al final de la palabra para buscar a los que finalizan
    if re.findall('^Sandra', elemento):
        print(elemento)

print("")

for nombre in lista_nombres:
    if re.findall('Martin$', nombre):
        print(nombre)


#Clase de caracteres: estos nos sirven para buscar caracteres, estos van dentro de corchetes
#y seran patrones de busqueda []
lista_dominios = ['https://elcoñigoascii.com',
                  'https://elcoñigoascii.es',
                  'https://elcodigoascii.gob']

lista_personas = ['hombres,'
                  'mujeres',
                  'mascotas',
                  'niños',
                  'niñas']

lista_autos = ['camion',
               'camión']

#Ejemplo con letra ñ en palabras
for caracter in lista_dominios:
    if re.findall('[ñ]', caracter):
        print(caracter)

#Ejemplo con letras ñ en dos casos
for caracter in lista_personas:
    if re.findall('[niñ[oa]s', caracter):
        print(caracter)
#Ejemplo con acento
for caracter in lista_autos:
    if re.findall('[cami[oó]n', caracter):
        print(caracter)