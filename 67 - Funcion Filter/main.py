#Forma parte de un grupo de funciones que se les denomina de orden superior y nos permiten utilizar un paradigma
#de programacion que se denomina programacion funcional
#La funcion filter comprueba que los elementos de una secuencia por ejemplo una lista, cumplan una condicion
#establecida devolviendo un iterador con los elementos que cumplen dicha condición

"""def numero_par(num):
    if num % 2 == 0:
        return True"""
#numeros = [17,24,7,39,8,51,92]

#La funcion filter recibe dos argumentos: nombre-funcion, lista y nos devuelve un objeto
#Para ver el objeto en formato de listas utilizamos el metodo list antes de la funcion filter
#print(list(filter(lambda numero_par: numero_par%2==0, numeros)))

#La funcion filter se utiliza mas para filtrar objetos que filtrar listas

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
Empleado("Juan", "Director", 75000),
Empleado("Ana", "Presidenta", 85000),
Empleado("Antonio", "Adminiostrativo", 25000),
Empleado("Sara", "Secretaria", 27000),
Empleado("Mario", "Botones", 21000),
]

salarios_altos = filter(lambda empleado:empleado.salario > 50000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)