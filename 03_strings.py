# Cadenas de texto
my_string = "Mi String"
other_string = 'Otro String'

print(len(my_string))
print(len(other_string))

print(my_string + " " + other_string)

# Algunos caracteres especiales
my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String \n escapado" #escapar caracteres especiales
print(my_scape_string)

# Formateo
name, surname, age = "Diego", "Chiapa", 32
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)