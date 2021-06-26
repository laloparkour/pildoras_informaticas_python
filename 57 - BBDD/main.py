#Como gestionar las claves principales de nuestra base de datos
#En una base de datos relacional los registros que se encuentran almacenados dentro de una tabla deben
#estar identificados cada uno de ellos de forma unica
#El campo clave identificara de forma unica a cada uno de nuestros registros
#Como crear base de datos que tengan tablas que cada uno de sus registros tenga campo clave y queden identificados
#de forkma unica

import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

#Podemos utilizar triple comilla para abrir y triple comilla para cerrar, esto es utili cuando nuestra
#instruccion va ser larga y queremos dividirla en varios renglones, si utilizamos una comilla norma, una comilla
#doble o una comilla sencilla estamos obligados a escribirlo en una sola linea
#La instruccion PRIMARY KEY tenemos que agregarsela al campo que queramos que sea clave
#Para crear un campo clave que incremento cada que creemos un registro debemos crear un campo que sea de
#tipo entero auto incrementable y esto lo hacemos agregando despues de la instruccion
#PRIMARY KEY LA INSTRUCCION AUTOINCREMENT y se le suele llamar campo ID
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

#No puede mas de un registro con el mismo nombre si es campo clave
productos = [
    ("Pelota", 20, "Juguetería"),
    ("Pantalón", 15, "Confección"),
    ("Desatornillador", 25, "Ferretería"),
    ("Jarrón", 20, "Cerámica")
]

#Si intentamos agregar un registro con el mismo campo clave este nos dara un error de tipo UNIQUE
#Cuando trabajamos con listas en bases de datos y tenemos un campo PRIMARY KEY autoincrementable
#debemos agregar en la parte de los campos que tiene nuestra tabla, en el campo ID autoincrementable
#debemos introducir la palabra reservada null, esto nos permite que python y el gestor de bases de datos
#gestione en automatico el campo clave
#Si queremos trabajar con otro campo  clave y otro campo que no se repita debemos agregar al campo la clausula UNIQUE
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()
miConexion.close()