#Aplicacion grafica tipo CRUD, conectarnos en una base de datos y realizar operaciones basicas
from tkinter import *
from tkinter import messagebox
import sqlite3

#----Funciones
def conexionBBDD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            NOMBRE VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if valor=="yes":
        root.destroy()

def limpiarCampos():
    varID.set("")
    varUser.set("")
    varPassword.set("")
    varNombre.set("")
    varApellido.set("")
    varDireccion.set("")
    formComentarios.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + varUser.get() +
                     "','" + varPassword.get() + "','" + varNombre.get() +
                     "','" + varApellido.get() + "','" + varDireccion.get() +
                     "','" + formComentarios.get("1.0", END) + "')")"""
    #Consulta Parametrizada
    #Guardar toda la informacion en una variable
    datos=varUser.get(), varPassword.get(), varNombre.get(), varApellido.get(), varDireccion.get(), formComentarios.get("1.0", END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?,?)", (datos))

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + varID.get())
    elUsuario=miCursor.fetchall()

    for usuario in elUsuario:
        varID.set(usuario[0])
        varUser.set(usuario[1])
        varPassword.set(usuario[2])
        varNombre.set(usuario[3])
        varApellido.set(usuario[4])
        varDireccion.set(usuario[5])
        formComentarios.insert(1.0, usuario[6])
    miConexion.commit()

def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    datos = varUser.get(), varPassword.get(), varNombre.get(), varApellido.get(), varDireccion.get(), formComentarios.get("1.0", END)
    """miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + varUser.get() +
                     "', PASSWORD='" + varPassword.get() +
                     "', NOMBRE='" + varNombre.get() +
                     "', APELLIDO='" + varApellido.get() +
                     "', DIRECCION='" + varDireccion.get() +
                     "', COMENTARIOS='" + formComentarios.get("1.0", END) + "' WHERE ID=" + varID.get())"""
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, "
                     "PASSWORD=?, "
                     "NOMBRE=?, "
                     "APELLIDO=?, "
                     "DIRECCION=?,"
                     "COMENTARIOS=?" + "WHERE ID=" + varID.get(), (datos))

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")

def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" +varID.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")

#----Interfaz Grafica
root = Tk()
#----Menu
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Eliminar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de..")

#----Campos
miFrame=Frame(root)
miFrame.pack()

#----Variables
varID = StringVar()
varUser = StringVar()
varPassword = StringVar()
varNombre = StringVar()
varApellido = StringVar()
varDireccion = StringVar()


labelID = Label(miFrame, text="ID:")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)
formID = Entry(miFrame, textvariable=varID)
formID.grid(row=0, column=1, padx=10, pady=10)

labelUser = Label(miFrame, text="Usuario:")
labelUser.grid(row=1, column=0, sticky="e", padx=10, pady=10)
formUser = Entry(miFrame, textvariable=varUser)
formUser.grid(row=1, column=1, padx=10, pady=10)

labelPassword = Label(miFrame, text="Password:")
labelPassword.grid(row=2, column=0, sticky="e", padx=10, pady=10)
formPassword = Entry(miFrame, textvariable=varPassword)
formPassword.grid(row=2, column=1, padx=10, pady=10)
formPassword.config(show="*", fg="Green")

labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=3, column=0, sticky="e", padx=10, pady=10)
formNombre = Entry(miFrame, textvariable=varNombre)
formNombre.grid(row=3, column=1, padx=10, pady=10)

labelAppellido = Label(miFrame, text="Apellido:")
labelAppellido.grid(row=4, column=0, sticky="e", padx=10, pady=10)
formApellido = Entry(miFrame, textvariable=varApellido)
formApellido.grid(row=4, column=1, padx=10, pady=10)

labelDireccion = Label(miFrame, text="Dirección:")
labelDireccion.grid(row=5, column=0, sticky="e", padx=10, pady=10)
formDireccion = Entry(miFrame, textvariable=varDireccion)
formDireccion.grid(row=5, column=1, padx=10, pady=10)

labelComentarios = Label(miFrame, text="Comentarios:")
labelComentarios.grid(row=6, column=0, sticky="e", padx=10, pady=10)
formComentarios = Text(miFrame, width=15, height=5)
formComentarios.grid(row=6, column=1, padx=10, pady=10)
scrollVertical = Scrollbar(miFrame, command=formComentarios.yview())
scrollVertical.grid(row=6, column=1, padx=10, pady=10, sticky="nse")
formComentarios.config(yscrollcommand=scrollVertical.set)

#---- Botones Inferiores
frameBotones=Frame(root)
frameBotones.pack()

btnCreate = Button(frameBotones, text="Create", command=crear).grid(row=0, column=0, padx=10, pady=10)
btnRead = Button(frameBotones, text="Read", command=leer).grid(row=0, column=1, padx=10, pady=10)
btnUpdate = Button(frameBotones, text="Update", command=actualizar).grid(row=0, column=2, padx=10, pady=10)
btnDelete = Button(frameBotones, text="Delete", command=eliminar).grid(row=0, column=3, padx=10, pady=10)

root.mainloop()