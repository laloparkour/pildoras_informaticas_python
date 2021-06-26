from tkinter import *
from tkinter import filedialog #la libreria filedialog nos permite crear ventanas emergentes para abrir archivos
#ventana emergente: abrir archivo

root=Tk()

def abreFichero():
    #el metodo filedialog nos permite crear una ventana emergente para abrir archivos de neustro equipo
    #y este nos devolvera como dato la ruta de el fichero que abrimos
    #este metodo recive diferentres parametros, el titulo, la ruta y el tipo de extencion de archivo que queremos examinar
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel", "*.xlsx"),
                                                                                    ("Ficheros de Texto", "*.txt"),
                                                                                    ("Todos los Ficheros", "*.*")))
    print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()