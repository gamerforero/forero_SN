def calcular_precio_entrada(edad):
    
    if edad < 4:
        return 0  
    elif 4 <= edad <= 18:
        return 30000  
    else:
        return 50000  


try:
    edad_cliente = int(input("Ingrese la edad del cliente: "))
    
    
    if edad_cliente < 0:
        raise ValueError("La edad debe ser un número positivo.")
    
    
    precio_entrada = calcular_precio_entrada(edad_cliente)

    if precio_entrada == 0:
        print("El cliente entra gratis.")
    else:
        print(f"El precio de la entrada es: {precio_entrada} pesos.")
except ValueError as e:
    print(f"Error: {e}. Por favor, ingrese una edad válida.")