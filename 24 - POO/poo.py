#La programacion orientada a objetos es trasladar el comportamiento
#de los objetos de la vida real a nuestro codigo para que el codigo
#tenga un comportamiento igual al de los objetos de la vida real

#Una clase: podemos definir como modelo donde se redactan las caracteristicas
#comunes de un grupo de objetos

#Objeto: Una instancia seria un objeto o ejemplar perteneciente a una clase

#Modularizacion: una aplicacion puede estar compuesta de varias clases, nos permite
#reutilizar codigo de un programa en otro, sirve tambien cuando un modulo o clase falla
#el programa sique funcionando excepto la clase o modulo dañado
#cada modulo funciona de manera independiente

#Encapsulacion: nos permite proteger del exterior una clase, para que nadie pueda manipularla
#Las clases en un sistema se conectan por medio de los metodos de acceso, para que
#funcionen como una unidad o un equipo, ala vez estan encapsuladas
#pero los metodos de acceso tendran acceso a siertas caracteristicas de cada una de las clases

#Para poder acceder a las propiedades y comportamineto de un objeto se utiliza
#lo que se conoce como nomenclatura del punto

#Acceder a propiedades
#nombre_del_objeto.propiedades = valor

#Acceder a comportamiento(que puede hacer mi objeto)
#nombre_del_objeto.comportamiento()

#sintaxis
#palabra reservada class nombre_clase():

#[Construimos la clase Coche]
"""class Coche():
    #[Creacion de uns constructor]
    #Podemos cambiar el valor de una variable encapsulada utilizando un metodo
    def __init__(self): #[Estado inicial]
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False #false = detenidos"""

#para establecer un comportamiento debemos de crear un metodo
#un metodo es una funcion especial que pertenece a la clase
#Nota: una funcion no pertenece a ninguna clase
#self hace referencia al propio objeto perteneciente a la clase (self = this en java o c++)
    #[Construimos Metodos]
"""def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche esta apagado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

    def __chequeo_interno(self):
        print("Reaizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False"""
#nombre_objeto = nombre_clase_para_objeto

#[Construimos Instancias]
#miCoche = Coche() #instanciar una clase o crear un objeto
#print(miCoche.arrancar(True)) #cambiar comportamiento
#miCoche.estado() #ver una propiedad
#print("A continuacion creamos el siguiente objeto")
#miCoche2 = Coche() #instanciar una clase o crear un objeto
#print(miCoche2.arrancar(False))
#miCoche2.estado()

#A la hora de utilizar POO es habitual que las caracteristicas comunes de los objetos formen parte de lo
#que se llama un estado inicial, esto significa que las caracteristicas o propiedades que tiene la clase la
#contengan los objetos nuevos
#Un constructor nos permite crear un estado inicial a los objetos pertenecientes a una clase
#Un constructor es un metodo especial que le da estado inicial a los objetos, es una forma de especificar
#claramente cual va ser el estado inicial de los objetos que pertenezcan a una clase

#Como creamos un metodo constructor
#Sintaxis
#def _init_(self): #De esta manera especificamos que este es el contructor de nuestra clase
#def _init_(self): #init = inicial

#Encapsulacion: consiste en encapsular o proteger una propiedad para que no se pueda modificar desde fuera
#Hacer que un metodo solo sea accesible dentro de la propia clase, no se puede acceder desde fuera
#Sintaxis
#self.__propiedad = valor (dos guiones bajos)

#Herencia: transladar el comportamiento de la herencia entre personas que ocurre en la vida real a codigo
#de programacion con algunas diferencias:
#A la primer clase se le llamaria clase padre o superclase
#La clase dos es a la vez clase padre o super clase y subclase
#Para que utilizamos la herencia en clases: nos permite reutilizar codigo en caso de crear objetos similares
#Sintaxis
#class nombre_clase(nombre_clase_de_la_que_heredamos)
#Herencia sobre escritura de metoddos: cuando una clase hereda un metodo de otra, se sobrescrive el metodo que hereda de la clase padre, es decir el metodo estado, invalida, anula
#sobreescrive el metodo de la clase padre
#Herencia Multiple: heredar de dos clases, consite en decirle dentro de los parentesis que vamos a heredar de dos clases o mas separandolos con coma
#en la herencia multiple se le da preferencia  siempre ala primera clase que indiques en la herencia multiple
#Herencia simple: heredar solamente de una clase
#funcion super(): nos permite llamar al metodo de la clase padre
#Principio de sustitucion: consiste en aplicar los terminos "es siempre un/a"
#La funcion isinstance = nos informa si un objeto es instancia de una clase determinada, esta devuelve True o False
    #Sintaxis
    #isinstance(nombre de instancia o objeto, nombre de clase a la que queremos comprobar si pertenece)
#Polimorfismo: un objeto puede cambiar de forma dependediendo del contexto que se utilize, al cambiar de forma cambia de comportamienito
#Tipado dinamico: no es necesario especificar de que tipo es un objeto a la hora de utilizarlo
class Vehiculos(): #creamos clase Vehiculos
    def __init__(self, marca, modelo): #Creamos constructor
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

miMoto = Moto("Honda", "CBR") #Creando objeto o instancia miMoto
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class bicicletaElectrica(VElectricos,Vehiculos):
    pass
miBici = bicicletaElectrica("Orbea", "hj1500")









