materia = ["Base de Datos", "Algebra", "Redes", "Computación", "Sistemas Operativos"]
materia_buscada = ""
for materia_individual in materia:
    print("- " + materia_individual)
materia_buscada = input("¿Qué materia buscas?")
if materia_buscada in materia:
    print(f"{materia_buscada} esta en tus materias")
else:
    print(f"{materia_buscada} no esta en tus materias")

#en linea 5 no hay espacios porque sino se ejecuta 5 veces diciendo una de las materias y preguntando, sin espacios
#el "for" termina de escribir todo para hacer la pregunta y ver si esta dentro de las materias
