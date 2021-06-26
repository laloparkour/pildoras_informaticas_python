#Funciones decoradoras con parametros

# Funcion decorador
def funcion_decoradora(funcion_parametro):
    #La nomenclatura *args nos permite decirle a una funcon que puede recibir un numero
    #indeterminado de parametros
    #La nomenclatura **kwargs nos permite decirle pasarle parametros con kwargs(argumentos con claves)
    def funcion_interior(*args, **kwargs):
        # Acciones adicionales que decoran
        print("Vamos a realizar un cálculo:")

        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")
    return funcion_interior

# Al agregar la nomenclatura  @nombre de la funcion decoradora estamos especificando que pasaremos como
# parametro la funcion parametro que seria la funcion suma
@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)
    
@funcion_decoradora
def potencia(base, exponente):
    print(pow(base,exponente))


suma(7,5,8)
resta(12,10)
#Ejemplo kwargs(argumentos con claves - clave-valor) clave = base y exponente, valor = 5 y 3
potencia(base=5, exponente=3)
