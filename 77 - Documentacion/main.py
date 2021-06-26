import math

def raizCuadrada(listaNumeros):
    """
    La función devuelve una lista con la raíz cuadrada de los elementos numéricos
    pasados por parámetros en otra lista
    Podemos agregar tres puntos ... para decirle a la zona de prueba la siguiente
    exprecion es una expresion anidada que pertenece a la linea anterior, para anidare
    expresiones, lineas de codigo utilizamos tres puntos
    >>> lista = []
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista = []
    >>> for i in [4, 9, 16, 50, 78, -90, 125]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    """
    #La funcion sqrt regresa un valor double
    return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9, 16, 25, 36]))

import doctest
doctest.testmod()