#Que es una inerfaz grafica: son ventanas con las que nosotros como usuarios interactuamos con los programas
#Una interfaz grafica es el intermediario entre el programa que se esta ejecutando y el usuario
#Tambien denominadas GUI (Grafic user interface)
#Se utiliza la libreria tkinder, aunque tambien esta wxPython, pyqt, pyGTK
#Tkinter es un puente entre python y la libreria TCL/TK

#Estructura de una interfaz grafica
#   Raiz(ventana)
#   Frame(organizador de elementos(widgets))
#   Widgets(botones, menus, etc)

from tkinter import *

raiz = Tk()

#Para dar titulo a una ventana se utiliza el metodo title("titulo)
raiz.title("Ventana de pruebas")

#Para evitar que la ventana se redomencione utilizamos el metodo resizable()
#Este recibe dos parametros, que el primero es al ancho y  segundo al alto y son de tipo boleanos
#raiz.resizable(0,0) #Pueden ser 0,0 o True, True

#Para cambiar el icono de la ventana utilizamos el metodo iconbitmap() y le pasamos el parametro la ruta
raiz.iconbitmap("pubg.ico")

#Para darle tamaño a la ventana utilizamos el metodo geometry() y le pasamos por parametro las medidas
raiz.geometry("650x350")

#El metodo config nos permite hacer varias cosas:
#Cambiar el color de fondo
raiz.config(bg="blue")

#Contruir Frame
miFrame = Frame()
#Empaquetar frame (meterlo dentro de la raiz), para empaquetar se utiliza el metodo .pack()
#Anclar en alguna posicion el frame(pasamos dentro del metodo pack como parametro la posicion)
#left, right, top, bottom
#para manejar dos opciones a la vez, pasamos como segundo parametro el metodo anchor
#los parametros a pasarle serian n, s, e, w
#miFrame.pack(side="left", anchor="n")
#Si queremos que el frame se expanda en alguna direccion utilizamos el metodo fill
#y le pasamos como paramertros (x, y, both)
#para que se expanda en el eje x utilizamos el parametro x
#para que se expanda en el eje y utilizamos el parametro y acompañado del metodo expand="True"
#para que se expanda en todas las direcciones utilizamos el parametro both acompañado del metodo expand="True"
#miFrame.pack(fill="y", expand="True")
#miFrame.pack(fill="both", expand="True")
miFrame.pack()

#para darle el grosor al borde utilizamos la propiedad bd
miFrame.config(bd="10")
#para cambiar las caracteristicas del borde utilizamos el metodo .config y le pasamos el parametro
#relief: "raised", "sunken", "flat", "groove", and "ridge"
miFrame.config(relief="groove")

#para cambiar el cursor utilizamos la propiedad cursor (hand2, pirate)
miFrame.config(cursor="pirate")

#Cambiar el color de fondo del frame
miFrame.config(bg="red")
#Darle tamaño a un frame, la raiz siempre se va a adaptar al tamaño de su contenedor interno
#Un frame tiene un tamaño fijo
miFrame.config(width="650", height="350")

#Todas las propiedades que se le dan al frame se le pueden dar a la raiz

#La instruccion mainloop es utilizada para que la ventana siempre este abierta como un buble infinito
#Una ventana debe de estar a la escucha de eventos
#El metodo mainoop debe de ir siempre al final
raiz.mainloop()