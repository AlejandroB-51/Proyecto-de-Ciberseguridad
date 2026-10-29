def mostrar_titulo():
    print("==================")
    print("Calculadora v2.0")
    print("==================")

def mostrar_opciones():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

mostrar_titulo()

while True:   #Ciclo para que no se cierre solo
    mostrar_opciones()
    operacion = input("Selecciona una opción (1-5): ")

    if operacion == "5":
        print("Cerrando la calculadora.")
        break  # Rompe el ciclo while

    if operacion not in ["1", "2", "3", "4"]:
        print("Opción inválida. Por favor, elige una opción del 1 al 5.\n")
        continue  # Vuelve al inicio del ciclo

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Debes ingresar un número válido. Inténtalo de nuevo.\n")
        continue  # Si ponen letras, reinicia el menú sin romper el programa

    if operacion == "1":
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}\n")
    
    elif operacion == "2":
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}\n")
    
    elif operacion == "3":
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}\n")
    
    elif operacion == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}\n")
        else:
            print("Error: No se puede dividir entre cero.\n")
