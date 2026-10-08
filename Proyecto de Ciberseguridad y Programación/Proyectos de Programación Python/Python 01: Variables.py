# variables

my_string_variable = "Mi Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_varible = str(my_int_variable)
print(my_int_to_str_varible)
print(type(my_int_to_str_varible))

my_bool_variable = False
print(my_bool_variable)

# concantenación de variables en un print (unir variables en un solo texto)
print (my_string_variable, my_int_to_str_varible, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# algunas funciones del sistema
print(len(my_int_to_str_varible))

#variables en una sola línea. !NO UTILIZAR EN EXCESO¡
name, surname, alias, age = "Alejandro", "Badillo", "INF Arqua", 12
print("Me llamo:", name, surname, "tengo",age,"años", "y mi alias es:",alias)

#input
"""
name = input("¿cual es tu nombre? ")
age = input("¿cuantos años tienes? ")

print(name)
print(age)
"""
#cambiamos su tipo
name = 12
age = "Alejandro"
print(name)
print(age)

# ¿forzamos el tipo?
addres: str = "mi dirección"
addres = True
addres = 5
addres = 1.2
print(addres)
print(type(addres))
