def Contraseña():
    contraseña_correcta = "nomeacuerdo"
    intentos = 3

    while intentos > 0:
        contraseña_ingresada = input("Ingrese la contraseña: ")
        if contraseña_ingresada == contraseña_correcta:
            print("Contraseña correcta,Acceso concedido")
            break
        else:
            intentos -= 1
            print(f"Contraseña incorrecta,Te quedan {intentos} intentos")

    if intentos == 0:
        print("Has agotado tus intentos,regresa en 30 minutos")