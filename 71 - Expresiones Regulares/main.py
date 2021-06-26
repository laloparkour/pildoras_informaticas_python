"""Rangos en expresiones regulares: los rangos nos permiten buscar elementos en una lista que
contengan por ejemplo un rango de caracteres o numeros, que comienzen o terminen por caracteres o numeros"""

import re

lista_nombres = ['Ana',
                 'Pedro',
                 'Maria',
                 'Rosa',
                 'Sandra',
                 'Celia']

for elemento in lista_nombres:
    if re.findall('[o-t]$', elemento):
        print(elemento)

lista_ciudades = ['Ma.1',
                 'Se1',
                 'Ma2',
                 'Ba1',
                 'Ma:3',
                 'Va1',
                 'Va2',
                 'Ma4',
                 'MaA',
                 'Ma.5',
                 'MaB',
                 'Ma:C']

for elemento in lista_ciudades:
    #Si anteponemos el acento en la lista de caracteres a buscar los negamos y busca todo excepto eso
    #if re.findall('Ma[^0-3]', elemento):
    if re.findall('Ma[.:]', elemento):
        print(elemento)