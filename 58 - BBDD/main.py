#Operaciones CRUD: CREATE, READ, UPDATE, DELETE)
#create : insertar o crear un nuevo registro
#read: leer informacion
#update: actualizar los registros de una base de datos
#delete: borrar la informacion los registros de una base de datos

import sqlite3

miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

#Clausula UNIDQUE: nos impide repetir la misma informacion en un campo de una tabla en una base de datos
"""miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos = [
    ("pelota", 20, "juguetería"),
    ("pantalón", 15, "confeccion"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica"),
    ("pantalónes", 35, "confeccion")
]"""

#Clausula INSERT nos permite insertar o crear datos
#miCursor.execute("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

#Clausula WHERE: la utilizamos para hacer una lectura
#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")
#productos=miCursor.fetchall()
#print(productos)

#Clausula UPDATE nombre_campo SET: nos permite actualizar registros
#Actualizar precio de una pelota
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#Clausula DELETE: nos permite borrar registros
#Si no incluimos la clausula WHERE en una instruccion DELETE estariamos borrando todos los registros en la base de datos
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()
miConexion.close()