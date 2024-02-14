def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        num = int(input("Ingresa un número para calcular su factorial: "))
        if num < 0:
            print("El factorial no está definido para números negativos.")
        else:
            print("El factorial de", num, "es:", factorial(num))
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()