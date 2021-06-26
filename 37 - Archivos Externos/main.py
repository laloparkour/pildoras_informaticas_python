#Que son los archivos externos?El objetivo de trabajar con archivos externos es la persistencia de datos, para ello utilizaremos
#archivos externos de texto usando el modulo estandar de python io.
#La persistencia de datos consiste en almacenar los datos que se han manejado durante la ejecucion del programa para que no se pierdan y tenerlos disponibles para un futuro
#Tenemos dos alternativas, guardarlos en archivos externos y guardarlos en bases de datos
#Archivos externos: hay de texto plano, binarios,
#Faces para guardar la informacion en archivos externos:
    #-Creacion
    #-Apertura(Abrirlo)
    #-Manipulacion
    #-Cierre

from io import open

#crear un archivo externo en modo escritura
#nombre_archivo = metodo open(nombre, modo(lectura, excritura, append(permite agregar informacion a un archivo que ya existe))
#archivo_texto = open("archivo.txt", "w")

#crearndo variable donde agreguemos texto
#frase = "Estupendo dia para estudiar python \n el domingo"

#agregar contenido al archivo
#nombre_archivo.write(argumento)
#archivo_texto.write(frase)

#cerrar archivo mediante python
#archivo_texto.close()


#abrir un archivo externo en modo lectura
#nombre_archivo = metodo open(nombre, modo(lectura, excritura, append(permite agregar informacion a un archivo que ya existe))
#archivo_texto = open("archivo.txt", "r")
#archivo_texto.seek(11)
#Si queremos situar el puntero en el centro de nuestro archivo de texto
#archivo_texto.seek(len(archivo_texto.read())/2)

#el metodo read nos permite leer la informacion de el archivo, si le pasamos un parametro este leera hasta
#texto = archivo_texto.read()

#el metodo readlines nos permite leer la informacion de un archivo y almacenarla en una lista
#lineas_texto = archivo_texto.readlines()
#archivo_texto.close()

#archivo_texto.seek()

#print(archivo_texto.read())
#print(texto)
#print(lineas_texto)
#si queremos ver una linea en especifico de nuestro texto especificamos el indice
#print(lineas_texto[0])

#abrir un archivo para agregar informacion
#nombre_archivo = metodo open(nombre, modo(lectura, excritura, append(permite agregar informacion a un archivo que ya existe))
#archivo_texto = open("archivo.txt", "a")

#archivo_texto.write("\n siempre es una buena ocacion para estudiar Python")
#archivo_texto.close()

#manejar un puntero dentro de un archivo de texto
#para ubicar el puntero en la posicion que queramos utilizamos el metodo seek(posicion en el archivo)
#nobre_archivo.seek(0)

#Para abrir un archivo en modo lectura y escritura
archivo_texto = open("archivo.txt", "r+")
#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()