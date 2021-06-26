#Widget text: sirve para introducir texto largo.
#Widget button: botones para interactuar con la interfaz

from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#Variables
miNombre = StringVar()

#Nombre
labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=0, column=0, sticky="w", padx=10, pady=10)
#Para asignar a nuestro formulario con nuestro boton utilizamos la instruccion
#textvariable=nombre_variable
formNombre = Entry(miFrame, textvariable=miNombre)
formNombre.grid(row=0, column=1, padx=10, pady=10)
formNombre.config(fg="red", justify="left")

#Apellido
labelApellido = Label(miFrame, text="Apellido:")
labelApellido.grid(row=1, column=0, sticky="w", padx=10, pady=10)
formApellido = Entry(miFrame)
formApellido.grid(row=1, column=1, padx=10, pady=10)

#Direccion
labelDireccion = Label(miFrame, text="Direccion:")
labelDireccion.grid(row=2, column=0, sticky="w", padx=10, pady=10)
formDireccion = Entry(miFrame)
formDireccion.grid(row=2, column=1, padx=10, pady=10)

#Password
labelPassword = Label(miFrame, text="Password:")
labelPassword.grid(row=3, column=0, sticky="w", padx=10, pady=10)
formPassword = Entry(miFrame)
formPassword.grid(row=3, column=1, padx=10, pady=10)
formPassword.config(show="*")

#Comentarios
labelComentarios = Label(miFrame, text="Comentarios:")
labelComentarios.grid(row=4, column=0, sticky="w", padx=10, pady=10)
textComentarios = Text(miFrame, width=15, height=5)
textComentarios.grid(row=4, column=1, padx=10, pady=10)
#Scrollbar: para indicarle la direccion del scrollbar se utiliza
#la instruccion command=(a quien pertenece.yview o xview)
#Para cambiar el diseño del scrollbar utilizamos la instruccion = ?
#Para ajustar el scrollbar al tamaño del cuadro de texto utilizamos
#la instruccion sticky="puntos cardinales"
#Para que el scroll bar quede incorporado en el widget text, se deja en la
#misma fila y columna, se le asigna el mismo padding y en el parámetro sticky= asigna el valor "nse".
scrollVert = Scrollbar(miFrame, command=textComentarios.yview)
scrollVert.grid(row=4, column=1, padx=10, pady=10, sticky="nse")
#Para que el posicionador de el scroll baje utilizamos en nuestro cuadro de comentarios el parametro
#yscrollcommand=nombre_scroll.set dentro de el metodo .config
textComentarios.config(yscrollcommand=scrollVert.set)

#boton
#Para crear un boton utilizamos la clase button
#Para agregar instrucciones a los botones utilizamos la instruccion command=
def codigoBoton():
    #la funcion set nos sirve para establecer un valor auna variable
    #para obtener informacion de un cuadro de texto utilizamos la funcion get
    miNombre.set("Laloparkour")

botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

miFrame.mainloop()