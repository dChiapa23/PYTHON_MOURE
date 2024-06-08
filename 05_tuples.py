# TUPLAS

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (32, 1.60, "Diego", "Chiapa")
my_other_tuple = (32, 60, 50, 45)
print(my_tuple)
print(type(my_tuple))

# Obtener un valor de una tupla
print(my_tuple[0])
print(my_tuple[-1])

# Contar la cantidad de valores iguales en una tupla
print(my_tuple.count("Diego"))

# Encontrar el indice del primer elemento que coincida en una tupla
print(my_tuple.index("Diego"))

# Concatenar tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) 

