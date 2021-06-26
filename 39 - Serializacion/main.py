#La serialización consiste en guardar en un fichero externo, una coleccion, un diccionario o incluso un objeto
#codificado en codigo binario(una sucesion de bytes)

#objetivo: nos permite distribuir un archivo, de manera codificada, para cuando lo necesitemos almacenar

#La biblioteca que se utiliza (Picle) y entre algunos metodos:
#Metodo: dump(): volcado de datos al fichero binario externo
#Metodo load(): carga de los datos del fichero binario externo

import pickle
#crear lista
lista_nombres = ["Pedro", "Ana", "Mariía", "Isabel"]

#crear fichero externo(nombre_fichero, tipo de escritura)
fichero_binario = open("lista_nombres", "wb")

#utilizar metodo dump para volcado de la lista al fichero externo (informacion a volcar, fichero a volcar)
pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

#borrado de memoria fichero
del(fichero_binario)

#leer archivo (nombre_archivo, tipo de lectura)
fichero = open("lista_nombres", "rb")


#guardar informacion del fichero
lista = pickle.load(fichero)

print(lista)