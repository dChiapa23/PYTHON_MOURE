# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,24,62,52,30,30,17]

print(my_list)
print(len(my_list))

my_other_list = [32, 1.60, "Diego", "Chiapa"]

print(type(my_list))
print(type(my_other_list))

# Acceder a un elemento especifico de una lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])

# Obtener la cantidad de veces que se repite un valor en una lista
print(my_list.count(30))

# Desempaquetar valores de una lista (Si o si hay que desempaquetar todos los valores)
age, height, name, surname = my_other_list
print(name)

# Concatenar listas
print(my_list + my_other_list)

# Agregar elementos al final de la lista
my_other_list.append("Hola")
print(my_other_list)

# Agregar elementos en el medio de la lista
my_other_list.insert(1, "rojo")
print(my_other_list)

# Editar un elemento de la lista
my_other_list[1] = "azul"
print(my_other_list)

# Eliminar elementos de la lista
my_other_list.remove("azul")
print(my_other_list)

my_list.remove(30) # Si un a lista tiene dos o mas valores iguales, elimina el primero de ellos
print(my_list)

# Eliminar un elemento por su indice, retornando el elemento (por defecto sera el ultimo)
my_list.pop()
print(my_list)

my_list.pop(2)
print(my_list)

# Eliminar un elemento por su indice, sin retornar el elemento
del my_list[2]
print(my_list)

# Copiar una lista
my_new_list = my_list.copy()

# Vaciar lista
my_list.clear()
print(my_list)
print(my_new_list)

# Dar vuelta una lista
my_new_list.reverse()
print(my_new_list)

# Ordenar una lista
my_new_list.sort()
print(my_new_list)
