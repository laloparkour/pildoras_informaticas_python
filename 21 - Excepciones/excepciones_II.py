def divide():
    try:
        n1 = float(input("Ingresa el primer numero: "))
        n2 = float(input("Ingresa el segundo numero: "))

        print("La division es: ", (n1/n2))
    except ValueError:
        print("El valor intrudicido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    finally:
        print("Calculo finalizado")
divide()