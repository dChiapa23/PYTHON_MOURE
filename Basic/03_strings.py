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
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# División de texto

# Selecciona una parte del texto
language_slice = language[1:3]
print(language_slice)
# Selecciona el final del texto empezando desde el carácter indicado
language_slice = language[1:]
print(language_slice)
# Selecciona un carácter del texto comenzando desde el final
language_slice = language[-2]
print(language_slice)
# Selecciona los caracteres que nosotros queremos
language_slice = language[0:6:2]
print(language_slice)

# Revertir texto
reversed_language = language[::-1]
print(reversed_language )

# Algunas funciones 
print(language.capitalize()) #Poner primera letra en mayúscula
print(language.upper()) #Poner texto en mayúsculas
print(language.lower()) #Poner texto en minúsculas
print(language.count("t")) #Contar cantidad de caracteres
print(language.isnumeric()) #Comprobar si un texto es un numero
print("1".isnumeric()) #Comprobar si un texto es un numero
print(language.upper().isupper()) #Comprobar si un texto esta en mayúsculas
print(language.lower().isupper()) #Comprobar si un texto esta en mayúsculas