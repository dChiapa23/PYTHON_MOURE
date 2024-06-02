# Variables

# Una buena practica es nombrar las variables con snake_case
my_string = "Hola"
print(my_string)
my_int = 5
print(my_int)
my_bool = True
print(my_bool)

# Podemos imprimir mas de una variable mediante una sola funcion print
print(my_string, my_int, my_bool)

# Transformar un numero u otro tipo de dato en string u otrp tipo de dato
my_int_to_string = str(my_int)
print(my_int_to_string,"tipo de dato:",type(my_int_to_string))

# Algunas funciones del Funciones del sistema

# len: devuelve el largo de una variable (cantidad de caracteres)
print(len(my_string))

#input: pide al usuario ingresar un dato
name = input("Cual es tu nombre? ")
age = input("Cual es tu edad? ")
print("EL nombre ingresado es:", name, ", la edad ingresada es:", age)

#las variables se pueden reasignar
name = "Diego"
age = 32
print("Mi nombre es:", name, ", mi edad es:", age)

# Incluso se puede cambiar el tipo de dato que guarda una variable, No es recomendable
name = 24
age = "Diego"
print("Mi nombre es:", name, ", mi edad es:", age)