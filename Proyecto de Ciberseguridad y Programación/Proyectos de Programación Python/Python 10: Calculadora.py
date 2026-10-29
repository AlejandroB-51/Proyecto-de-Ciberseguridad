def mostrar_titulo():
    print("==================")
    print("Calculadora v1.0")
    print("==================")
def mostrar_opciones():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
mostrar_titulo()
mostrar_opciones()
def opciones ():
    operacion: str = input("Selecciona una opción: ") #str es el tipo de dato que se espera recibir, en este caso texto
    if operacion == "1":
        num1 = float(input("Ingresa el primer número: ")) #float() convierte el valor ingresado a un número decimal
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
        otra_operacion = input("¿Quieres realizar otra operación? (s/n): ")
        if otra_operacion.lower() == "s": #lower() convierte el texto en minúsculas
            mostrar_opciones()
            opciones()
        else:
             print("Cerrando la calculadora.")
    if operacion == "2":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
        otra_operacion = input("¿Quieres realizar otra operación? (s/n): ")
        if otra_operacion.lower() == "s":
                    mostrar_opciones()
                    opciones()
        else:
            print("Cerrando la calculadora.")
    if operacion == "3":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
        otra_operacion = input("¿Quieres realizar otra operación? (s/n): ")
        if otra_operacion.lower() == "s":
            mostrar_opciones()
            opciones()
        else:
            print("Cerrando la calculadora.")
    if operacion == "4":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
            otra_operacion = input("¿Quieres realizar otra operación? (s/n): ")
            if otra_operacion.lower() == "s":
                        mostrar_opciones()
                        opciones()
            else:
                print("Cerrando la calculadora.")
        else:
            print("Error: No se puede dividir entre cero.")
            otra_operacion = input("¿Quieres realizar otra operación? (s/n): ")
            if otra_operacion.lower() == "s":
                        mostrar_opciones()
                        opciones()
            else:
              print("Cerrando la calculadora.")
    if operacion == "5":
        print("Cerrando la calculadora.")
opciones()
