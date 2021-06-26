#Documentacion: incluir comentarios en clases, métodos, módulos etc.
#Para que sirven los comentarios: para ayudar en el trabajo en equipo.
#Especialemnte útil en aplicaciones complejas. Nos permiten explicar que hace cada cosa

class areas:
    """Esta clase calcula las áreas de diferentes figuras geométricas"""
    def areaCuadrado(lado):
        """Estas funcion calcula el área de un cuadrado, elevando al cuadrado el lado, pasando por
        parámetro"""

        return "El area del cuadreado es: " + str(lado*lado)

    def areaTriangulo(base, altura):
        """Calcula el area de un triángulo utilizando los parámetrops base y altura"""

        return "El área del triángulo es: " + str((base*altura)/2)


    #print(areaCuadrado(3))
    #print(areaTriangulo(2,7))

    #La funcion: nombre-funcion.__doc__ nos permite imprimir la documentacion asociada a la funcion en la cual
    #tenemos documentacion
    #print(areaCuadrado.__doc__)

    #La instruccion help(nombre_funcion) nos ofrece la definicion de la funcion con el parametro
    #y la documentacion
    #help(areaTriangulo)

    #Cuando la funcion pertenece a una clase, primero debemos utilizar el nombre de la clase y despues
    #el de la funcion
    #help(areas.areaTriangulo)

#Podemos obtener una ayuda de toda la clase
help(areas)