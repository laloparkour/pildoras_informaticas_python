#Ventanas emergentes: son ventanas modales para informar, avisas o permitir realizar tareas aL usuario
#la libreria messagebox() nos permite crear ventanas emergentes
from tkinter import messagebox
from tkinter import *

root=Tk()

#funciones
def infoAdicional():
    #el metodo .showinfo() nos permite crear ventanas emergentes de tipo infoprmativas
    #y este lleva como parametros, el texto del titulo y el texto de la ventana
    messagebox.showinfo("Procesador de Laloparkour", "Procesador de textos 2020")

def avisoLicencia():
    #el metodo .showwarning() nos permite crear ventanas emergentes de tipo aviso y llevan como
    #parametros el titulo y el texto de la ventana emergente
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
    #el metodo .askquestion() nos permtie crear ventanas emergentes de tipo pregunta y este lleva
    #como parametro tanto el titulo como, el texto de la ventana emergente
    #este metodo devuelve dos valores, yes o no
    #valor=messagebox.askquestion("Salir", "Deseas salir de la aplicacion")

    #el metodo .askokcancel() nos permite crear ventanas emergentes de tipo pregunta a diferencia
    #del metodo .askquestion este tiene como opciones aceptar o cancelar y nos devuelve dos valores
    #boleanos true o false
    valor=messagebox.askokcancel("Salir", "Deseas salir de la aplicacion")
    if valor==True:
        root.destroy()

def cerrarDocumento():
    #el metodo .askretrycancel() nos permite crear ventanas emergentes de tipo reintento a y estas
    #llevan como parametros tanto el titulo como el texto de la ventana, en la ventan tenemos dos
    #opciones que deuvelven valores booleanos y son reitentar=true y cancelar=false
    valor = messagebox.askretrycancel("Reintentar", "No es pocible cerrar documento bloqueado")
    if valor==False:
        root.destroy()


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

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
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)

root.mainloop()