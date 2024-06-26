# Gestor de paquetes de Python

# pypi.org

import numpy

print(numpy.version.version)

numpy_array = numpy.array([35,24,62,52,30,30,17])
print(type(numpy_array))
print(numpy_array * 2)

# pip list
# pip uninstall pandas
# pip show pandas
# pip install requests

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.json())

# Paquete Arithmetics
from package import arithmetics

print(arithmetics.sum(5,2))