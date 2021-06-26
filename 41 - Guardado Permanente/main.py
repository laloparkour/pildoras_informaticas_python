#Guardar datos de forma permanente en ficheros

import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de:", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero esta vacío")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaPersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaPersonas)
        listaPersonas.close()
        del(listaPersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista = listaPersonas()
persona = Persona("Ana", "Femenino", 19)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
