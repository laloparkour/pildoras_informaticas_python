#Widget entry(formulario): este widget es utilizado para introducir texto
#Las opciones que tenemos en los label, podemos utilizarlas tambien en los entry

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=0, column=0, sticky="w", padx="10", pady="10")

formNombre = Entry(miFrame)
#metodo grid: es una tabla con tantas filas y columnas como nosotros queramos
#divide nuestra interfaz en casillas
#El metodo grid lleva dos parametros: fila y columna
formNombre.grid(row=0, column=1, padx="10", pady="10")

labelPassword = Label(miFrame, text="Contraseña:")
labelPassword.grid(row=1, column=0, sticky="w", padx="10", pady="10")
formPassword = Entry(miFrame)
formPassword.grid(row=1, column=1, padx="10", pady="10")
#El metodo config nos permite utilizar la propiedad config donde por parametro le pasamos el atributo
#show="*" y este nos mostrara asteriscos al escribir en el cuadro de texto o cualquier caracter que queramos
formPassword.config(show="*")

labelApellido = Label(miFrame, text="Apellido:")
labelApellido.grid(row=2, column=0, sticky="w", padx="10", pady="10")
formApellido = Entry(miFrame)
formApellido.grid(row=2, column=1, padx="10", pady="10")

labelDireccion = Label(miFrame, text="Dirección:")
labelDireccion.grid(row=3, column=0, sticky="w", padx="10", pady="10")
formDireccion = Entry(miFrame)
formDireccion.grid(row=3, column=1, padx="10", pady="10")

#Podemos alinear los textos de nuestros label utilizando la propiedad sticky:
#los valores que se le pueden dar son: n(north), s(south), e(east), w(west), estos tambien
#tienen puntos intermedios los cuales serian, ne, se, sw, nw(northeast, southeast, southwest, northwest)
#sintaxis = sticky="w"
#El padding nos permite separar nuestros elementos de los bordes para que no se vean tan juntos
#Cualquier elementos tiene un contenedcor padre, el padding es la distancia que hay de nuestro
#contenedor padre, hasta el limite del contenedor padre
#En python tenemos el pady(vertical) y el padx(horizontal)

raiz.mainloop()
