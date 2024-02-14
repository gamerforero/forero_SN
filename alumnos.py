def main():
    num_alumnos = int(input("Ingrese el número de alumnos: "))
    alumnos_notas = {}

    for _ in range(num_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")

        if nombre in alumnos_notas:
            print("¡Error! Este alumno ya ha sido registrado.")
            continue

        notas = []
        nota = float(input(f"Ingrese la nota del alumno {nombre} (-1 para terminar): "))
        
        while nota >= 0:
            notas.append(nota)
            nota = float(input("Ingrese la siguiente nota (-1 para terminar): "))

        alumnos_notas[nombre] = notas

    print("\nLista de alumnos y sus promedios:")
    for alumno, notas in alumnos_notas.items():
        promedio = sum(notas) / len(notas)
        print(f"{alumno}: {notas} - Promedio: {promedio}")

if __name__ == "__main__":
    main()