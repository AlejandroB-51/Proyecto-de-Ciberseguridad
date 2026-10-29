import random
import string

print("=== Generador de Contraseñas ===")

def contraseña_random(longitud): #(length) es la longitud para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation #caracteres que se pueden usar en la contraseña
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud)) #generar la contraseña
    return contraseña

while True:
    try: 
        longitud = int(input("Ingrese la longitud que desea para la contraseña:")) 
        break
    except ValueError:  
        print("La longitud debe ser un número entero, por favor intentelo denuevo.")

#La función del ciclo while (incluyendo try... except) es evitar que se coloquen valores que no sean numero enteros
pass

while longitud < 6:
    print("La longitud de la contraseña debe contener un mínimo de 6 caracteres. Vuelva a intentarlo:")
    while True:
        try:
            longitud = int(input("Ingrese la longitud que desea para la contraseña: "))
            break
        except ValueError:
            print("La longitud debe ser un número entero, por favor inténtelo de nuevo.")

#se usa un ciclo while para evitar que el usuario coloque un valor menor de 6
pass

if longitud >= 6:
    contraseña = contraseña_random(longitud)
    print(f"Su contraseña ha sido generada. Su contraseña es: {contraseña}")
