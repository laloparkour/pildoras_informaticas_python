#widget menu
from tkinter import *

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#Menu
#el metodo .menu nos permite crear un elemento en un menu
#para quitar la barra separadora que se crea en nuestros menus agregamos el parametro tearoff=0 en nuestro
#mertodo Menu()
archivoMenu=Menu(barraMenu, tearoff=0)

#-------Archivo
#el metodo add_cascade nos permite agregarle caracteristicas a un elemento de un menu, este recibe parametros
#label=texto del elemento, menu=ubicacion del elemento
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
#el metodo .add_command nos permite agregar submenus a nuestros elementos del menu, este recibe parametros
#al  igual que el elemento del menu, label=texto elemento,
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
#Para crear una barra separadora utilizamos el metodo add_separator()
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

#-------Edicion
archivoEdicion=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Borrar")

#-------Herramientas
archivoHerramientas=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

#-------Ayuda
archivoAyuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de")


root.mainloop()