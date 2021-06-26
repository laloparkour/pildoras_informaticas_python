"""
Decoradores o funciones decoradoras: son funciones que a su vez añaden funcionalidades a otras
funciones que ya exitan en tu programa

Una funcion decorador esta formado por 3 funciones, A, B y C, donde a recibe un parámetro a B para
devolver C.
Un decorador devuelve una funcion

Sintaxis:
def funcion_decorador A(funcion B):
    def funcion interna C():
        codigo de la funcion interna C
    return funcion interna C
"""

# Funcion decorador
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        # Acciones adicionales que decoran
        print("Vamos a realizar un cálculo:")

        funcion_parametro()

        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")
    return funcion_interior

# Al agregar la nomenclatura  @nombre de la funcion decoradora estamos especificando que pasaremos como
# parametro la funcion parametro que seria la funcion suma
@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()



