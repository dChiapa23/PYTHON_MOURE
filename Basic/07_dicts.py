# Diccionarios

my_dict = dict()
my_other_dict ={}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"name": "Diego", "surname":"Chiapa", "Age": 32}
my_dict = {
  "name": "Diego",
  "surname":"Chiapa",
  "Age": 32,
  "languages": {"JavaScript", "TypeScript", "Python"}
  }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

# Obtener un valor por su clave
print(my_dict["name"])

# Actualizar un valor
my_dict["name"] = "Ezequiel"
print(my_dict["name"])

# Agregar un nuevo par clave:valor
my_dict["Address"] = "Alberti 468"
print(my_dict)

# Eliminar un valor
del my_dict["Address"]
print(my_dict)

# Buscar si un elemento existe en un diccionario por su clave
print("Chiapa" in my_dict)
print("surname" in my_dict)

# Obtener todos los items de un diccionario
print(my_dict.items())
# Obtener todas las claves de un diccionario
print(my_dict.keys())
# Obtener todos los valores de un diccionario
print(my_dict.values())

# Crear un diccionario con calves, sin valores
my_new_dict = dict.fromkeys(("Nombre", "Apellido", "Edad"))
print(my_new_dict)

# Crear un diccionario donde todas las claves tendrán el mismo valor
my_new_dict = dict.fromkeys(("Nombre", "Apellido", "Edad"), ("Diego"))
print(my_new_dict)