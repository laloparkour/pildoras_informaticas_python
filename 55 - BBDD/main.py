#Pasos a seguir para conectarnos con una base de datos:
#1- Abrir-Crear Conexión
#Crear puntero
#Ejecutar query(consulta) SQL
#Manejar los resultados de la query(consulta - CRUD)
#Insertar, Leer, Actualizar, Borrar(Create, Read, Update, Delete)
#Cerrar puntero
#Cerrar conexión

#Importar libreria sqlite
import sqlite3

#crear una coneccion en sqlite
miConexion=sqlite3.connect("PrimeraBase")

#Crear tabla en sqlite
#Primero debemos crear nuestro puntero o cursor
miCursor=miConexion.cursor()

#Ejecutar query(consultas)
#Se debe de invalidar al momento de ejecutar el programa por segunda vez para que este no cree nuevamente la tabla
#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#Como insertar datos en una tabla
#Al anidar comillas en python si utilizamos comillas dobles primero, las segundas se utilizan simples y viceversa
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

#Cada que generamos un cambio, tenemos que verificar que querermos hacer el cambio
#utilizando  nuestra coneccion con el metodo .commit(), este significa que confirmamos
miConexion.commit()

#Cerrar coneccion en sqlite
miConexion.close()