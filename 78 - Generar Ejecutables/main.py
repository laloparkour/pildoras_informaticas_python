"""
Crear ejecutables; el ejecutable toma la extencion de el sistema operativo que estemos
utilizando (.exe, tar.gz)
Para crear un ejecutable ocupamos instalar py installer, despues vamos al directorio
donde tenemos la aplicacion y utilizamos el comando pyinstaller nombre_archivo a convertir
Para que no nos aparezca la consola detras de la aplicacion, agregamos un modificador a la instruccion
y seria pyinstaller --windowed nombre_archivo a convertir
Para que no necesite de todos los archivos que genera, y poder ejecutarlo en cualquier ordenador
agregamos un modificador mas que seria pyinstaller --windows --onefile nombre_archivo a convertir
Para agregar un icono debemos acompañar el archivo a convertir en la misma carpeta dodne esta ubicado
con una imagen en formato .ico y agregamos el modificador --icon=./nombre icono
"""

