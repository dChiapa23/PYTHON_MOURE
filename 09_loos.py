# Bucles

# Bucle While
my_condition = 0

while my_condition < 10:
  print(my_condition)
  my_condition += 2

# Se puede agregar un else a un while
my_condition = 0
while my_condition < 10:
  print(my_condition)
  my_condition += 2
else: # Es opcional
  print("Mi condición es mayor o igual a 10")

print("La ejecución continua")

while my_condition < 20:
  my_condition += 1
  if my_condition == 15:
    print("Mi condición es 15")
    break
  print("Mi condición es menor a 20")
print("La ejecución continua")

# Bucle For

my_list = [35,24,62,52,30,30,17]

for element in my_list:
  print(element)
print("Imprimi my_list")

my_tuple = (32, 1.60, "Diego", "Chiapa")
my_set = {"Diego", "Chiapa", 32}
my_dict = {"name": "Diego", "surname":"Chiapa", "Age": 32}

for element in my_tuple:
  print(element)
else:
  print("Imprimi my_tuple")
for element in my_set:
  print(element)
else:
  print("Imprimi my_set")
for element in my_dict:
  print(element)
  if element == "surname":
    break
else:
  print("Imprimi my_dict")
print("La ejecución continua")

for element in my_dict:
  print(element)
  if element == "surname":
    continue
  print("Se ejecuta")
else:
  print("Imprimi my_dict")
print("La ejecución continua")