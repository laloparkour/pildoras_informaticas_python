#metodos de cadenas: python considera a las cadenas de caracteres de decir a las palabras, las frases, las letras, objetos, estos objetos se denominan strings,
#como objetos que son tienen sus propiedades y sus metodos

#upper(): construye en mayusculas todas las letras de un string
#lower(): construye a minuscuas todas las letras de un string
#capitalyze(): en una string pone la primera letra en mayuscula
#count(): cuenta cuantas veces aparece una letra o una cadena de caracteres, un grupo de letras dentro de un texto o una frase
#find(): representa el indice, la posicion en la cual aparece un caracter o un grupo de caracteres dentro de un texto
#isdigit(): devuelve un booleano, nos dice si el valor intruducido es un digito, es un valor numerico o no lo es
#isalum(): comprueba si los caracteres intruducidos son alfanumerico
#isalpha(): comprueba si los caracteres introducidos son solo letras, los espacios no cuentan
#split(): separa por palabras utilizando espacios
#strip(): borra los espacios sobrantes al principio y al final
#replace(): cambia una palabra o una letra por otra en un string
#rfind(): representa el indice, la posicion en la cual aparece un caracter o un grupo de caracteres dentro de un texto comenzando desde el final

nombreUsuario = input("Introduce un nombre de usuario:")

#como se utilizaban los metodos de los objetos (objetos.metodos)
print("El nombre es:", nombreUsuario.upper())
print("El nombre es:", nombreUsuario.lower())
print("El nombre es:", nombreUsuario.capitalize())

edad = input("Introduce la edad:")

while (edad.isdigit() == False):
    print("Por favor introduce un valor numerico: ")
    edad = input("Introduce la edad:")

if (int(edad >= 18):
    print("Puede pasar")
else:
    print("No puede pasar")
