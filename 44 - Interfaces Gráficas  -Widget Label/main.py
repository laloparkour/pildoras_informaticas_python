#Widget Label: nos permiten mostrar texto o imágenes
#Tienen como única finalidad mostrar texto, no se puede interactuar con él(borrar, arrastrar)

#Sintaxis
#variable = Label(contenedor, opciones)
#Opciones
#Text: texto que se muestra en el label
#Anchor: controla la posición del texto si hay espacio suficiente para él(center por defecto)
#Bg: color de fondo
#Bitmap: mapa de bits que se mostrará como gráfico
#Bd: grosor del boprde (2px por defecto)
#Font: tipo de fuente a mostrar
#Fg:  color de la fuente
#Width: ancho del label en caracteres(no en píxeles)
#Height: altura del label en caracteres(no en píxeles)
#Image: muestra image en el label en lugar de texto
#Justify: justificacion del texto del label

from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)
miFrame.pack()

#La clase PhotoImage nos permite rescatar y manipular imagenes
miImagen = PhotoImage(file="ongo.png")
labelImagen = Label(miFrame, image=miImagen)
labelImagen.place(x=100, y=3000)

miLabel = Label(miFrame, text="Hola Alumnos de Python", fg="red", font=("Comic Sans MS", "18"))
miLabel.place(x=100, y=200)
#El metodo place nos permite ubicar el texto en nuestra interfaz grafica por medio de coordenadas
#miLabel.place(x=100, y=200)

root.mainloop()

