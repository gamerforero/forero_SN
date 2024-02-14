def ejercicio1():
    print("Ejecutando Ejercicio 1")

def ejercicio2():
    print("Ejecutando Ejercicio 2")

def ejercicio3():
    print("Ejecutando Ejercicio 3")

while True:
    print("\nMenú Principal:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")