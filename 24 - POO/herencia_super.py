class persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre #campo de clase o variable de clase
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Lugar de residencia:", self.lugar_residencia)

class empleado(persona):
    def __init__(self, salario, antiguedad, puesto, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
        self.puesto = puesto

    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario)
        print("Antiguedad:", self.antiguedad)
        print("Puesto:", self.puesto)

#isaac = persona("Isaac", 27, "La Paz")
#isaac.descripcion()


isaac = persona("Isaac", 27, "Mexicano")
isaac.descripcion()
print(isinstance(isaac, empleado))