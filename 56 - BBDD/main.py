import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

#Podemos insertar varios elementos en una base de datos trabajando con tuplas
#El metodo .execute nos permite insertar un registro

#variosProductos = [
#    ("Camiseta", 10, "Deportes"),
#    ("Jarrón", 40, "Cerámica"),
#    ("Camión", 20, "Juguetería")
#]

#Para insertar mas registros podemos utilizar el metodo .executemany
#como parametro recibe la instruccion sql de tipo
#("INSERT INTO nombre_tabla VALUES (? se utilizan las interrogantes tantos como campos queramos utilizar)", nombre_tupla)
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

#Para leer informacion de una base de datos utilizamos la instruccion SELECT
miCursor.execute("SELECT * FROM PRODUCTOS")

#Para ver la informacion ocupamos crear una lista para almacenar los registos y utilizamos el metodo fetchall()
#para que este nos devuela los valores dentro de la lista creadas
variosProductos = miCursor.fetchall()
#Para ver los elementos de la lista utilizamos un print(variosProductos)

#Tambien podemos ver los elementos de una lista utilizando un ciclo for
for producto in variosProductos:
    print("Nombre articulo:", producto[0],
          "Seccion:", producto[2],
          "Precio:", producto[1])
miConexion.commit()

miConexion.close()