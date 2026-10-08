# Strings #

my_string = "Mi String"
my_other_string = "Mi otro string"

print(len(my_string)) #len = longitud
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un sting\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un sting con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un sting \n escapado"
print(my_scape_string)

#Formateo de strings

name, surname, age = "Alejandro", "Badillo", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Despaqueando caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
