numero_Secreto = 42 
adivinar = 0
while adivinar != numero_Secreto:
    adivinar = int(input("Adivina el numero secreto "))
    if adivinar < numero_Secreto:
        print("Número muy bajo, intenta de nuevo")
    elif adivinar > numero_Secreto:
        print("Número muy alto, intenta de nuevo")
    else:
        print("¡Correcto! era el 42")

#el valor de "while" o que busca en este caso "adivinar" siempre debe ir antes con un valor distinto
#para números principalmente es 0 y para texto " "
