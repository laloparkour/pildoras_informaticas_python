email = input("Introduce un correo: ")

arroba = email.count("@")
if (arroba != 1 or email.find("@") == 0 or email.rfind("@") == len(email)-1):
    print("Email Incorrecto")
else:
    print("Email Correcto")
