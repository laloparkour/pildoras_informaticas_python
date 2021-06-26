#Utilizar la documentación para realizar pruebas
#Modulo doctest

#def areaTriangulo(base, altura):
    """
    Calcula el área de un triángulo dado
    Como hacer un test o prueba utilizando la documentacion: nos situamos entre las
    comillas de apertura y las comillas de cierre, colocamos tres parentesis angulares
    o simbolos de mayor que, nombre de la funcion y le pasamos los parametros()
    y debajo debemos de escribir lo que la funcion deberia devolver con los parametros
    que le pasamos

    >>> areaTriangulo(3,6)
    9.0

    """
    #return (base*altura)/2

#print(areaTriangulo(2,4))

#import doctest
#doctest.testmod()
#Si la funcion no devuelve ningun valor significa que la funcion esta correcta
#de lo contrario esta nos informara del error

def compruebaCorreo(correo):

    """
    La funcion comprueba correo evalúa un correo recibido en busca
    de la @. Si tiene una @ es correcto, si tiene más de una @ es incorrecto,
    si la @ está al final es incorrecto.

    >>> compruebaCorreo('lalo@cursos.com')
    True

    >>> compruebaCorreo('juancursos.es@')
    False

    >>> compruebaCorreo('juancursos.es')
    False

    >>> compruebaCorreo('juan@cursos.es@')
    False

    """

    arroba = compruebaCorreo.count('@')
    if(arroba!=1 or compruebaCorreo.rfind('@')==(len(compruebaCorreo)-1) or
    compruebaCorreo.find('@')==0):
        return False
    else:
        return True

import doctest
doctest.testmod()