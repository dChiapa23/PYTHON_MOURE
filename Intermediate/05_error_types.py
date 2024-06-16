# Tipos de error

# SyntaxError
# print "Hola comunidad"
print("Hola comunidad")

# NameError
# print(language)
language = "Spanish"
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
#print(my_list[5])
print(my_list[4])

# ModuleNotFoundError
#import maths
import math

# AttributeError
# print(math.PI)
print(math.pi)

# KeyError
my_dict = {"name": "Diego", "surname":"Chiapa", "Age": 32, "languages": {"JavaScript", "TypeScript", "Python"}}
# print(my_dict["AGE"])
print(my_dict["Age"])

# TypeError
# print(my_list["4"])
print(my_list[4])

# ImportError
# from math import PI as PI_VALUE
from math import pi as PI_VALUE

# ValueError
# my_int = int("10 A")
my_int = int("10")

# ZeroDivisionError
# result = 10/0
result = 10/1