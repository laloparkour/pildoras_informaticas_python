from tkinter import *
#Check Buttons: son botones de selección para preguntas de respuesta múltiplea

root = Tk()
root.title("Ejemplo")

#Variables
playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+="Playa"

    if(montana.get()==1):
        opcionEscogida+="montana"

    if(turismoRural.get()==1):
        opcionEscogida+="turismoRural"

    textoFinal.config(text=opcionEscogida)

#foto=PhotoImage(file="avion.png")
#Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

#sintaxis [ubicacion, texto]
#onvalue = si esta seleccionado o se selecciona
#offvalue = si esta deseleccionado o se quita la seleccion

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje()).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje()).pack()
Checkbutton(frame, text="Turismo Rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje()).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()
