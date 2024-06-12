# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Diego", "Chiapa", 32}
print(type(my_other_set))
print(my_other_set)

my_other_set.add("DChiapa") # Un set es una estructura desordenada
print(my_other_set)

my_other_set.add("DChiapa") # Un set no admite elementos repetidos
print(my_other_set)

print("Chiapa" in my_other_set) # Comprobar si un elemento existe en un set
print("Chapa" in my_other_set)

my_other_set.remove("Chiapa") # Eliminar un elemento de un set
print(my_other_set)

my_other_set.clear() # Vaciar un set
print(my_other_set)
print(len(my_other_set))

del my_other_set # Eliminar un set.

my_set = {"Diego", "Chiapa", 32}
my_other_set = {"JavaScript", "Python"}

my_new_set = my_set.union(my_other_set) # Unir sets con valores diferentes
print(my_new_set)

print(my_new_set.difference(my_set)) # Obtener los valores que están en my_new_set pero no en my_set