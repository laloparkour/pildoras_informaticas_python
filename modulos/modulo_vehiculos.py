class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.encendido = True
    def acelerar(self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEncendido: ", self.encendido, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEncendido: ", self.encendido, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\nCaballito: ", self.hcaballito)

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100
    def cargarEnergia(self):
        self.cargando = True