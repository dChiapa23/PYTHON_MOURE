# Funciones

def my_function ():
  print("Mi función")

my_function()

def sum_two_values (first_value, second_value):
  print(first_value + second_value)

sum_two_values(5, 6)
sum_two_values(5, 6.5)

def sum_two_values_return (first_value, second_value):
  return first_value + second_value

my_result = sum_two_values_return(10,5)
print(my_result)

def print_name (name, surname):
  print(f"My name is: {name} {surname}")

print_name(surname = "Chiapa", name = "Diego")

def print_name_default (name, surname, alias = "Sin alias"):
  print(f"My name is: {name} {surname} {alias}")

print_name_default("Diego", "Chiapa", "DChiapa")
print_name_default("Diego", "Chiapa")

def print_upper_texts(*texts):
  for text in texts:
    print(text.upper())

print_upper_texts("Hola", "python", "DCHIAPA")
