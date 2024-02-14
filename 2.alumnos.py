def obtener_grupo(nombre, sexo):
    if (sexo == 'mujer' and nombre.lower() < 'm') or (sexo == 'hombre' and nombre.lower() >= 'n'):
        return 'Grupo A'
    else:
        return 'Grupo B'

nombre = input("Escriba su nombre: ")
sexo = input("Ingrese su sexo: ").lower()

grupo = obtener_grupo(nombre, sexo)
print(f"Tu grupo es: {grupo}")