import random

def tirar_dado():
    
    return random.randint(1, 6)

def jugar_juego():
    
    resultado_alvaro = tirar_dado()
    print("Álvaro tiró un", resultado_alvaro)

    resultado_barbara = tirar_dado()
    print("Bárbara tiró un", resultado_barbara)

    if resultado_alvaro > resultado_barbara:
        print("¡Álvaro gana!")
    elif resultado_alvaro < resultado_barbara:
        print("¡Bárbara gana!")
    else:
        print("¡Empate!")

jugar_juego()