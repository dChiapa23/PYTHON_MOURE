# Manajeno de ficheros

import os

# Fichero .txt

if not os.path.isfile("Intermediate/my_file.txt"):
  txt_file = open(file="Intermediate/my_file.txt", mode="w+") # Escribir y mas
  txt_file.write("Mi nombre es Diego\nMi apellido es Chiapa\nTengo 32 años\nY mi lenguaje preferido es Python")
  txt_file.close()
  print("Se ha creado el archivo: my_file.txt")

txt_file = open(file="Intermediate/my_file.txt", mode="r+") # Leer y Escribir
# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
#print(txt_file.readlines())

lines_file = txt_file.readlines()

for line in lines_file:
  print(line)

if "Aunque tambien me gusta JavaScript" not in lines_file:
  txt_file.write("\nAunque tambien me gusta JavaScript")
  print("\nAdded line: Aunque tambien me gusta JavaScript")

txt_file.close()

# os.remove("Intermediate/my_file.txt")

# Fichero .json

import json

json_file = open("Intermediate/my_file.json", "w+")

json_test = {"name": "Diego", "surname":"Chiapa", "age": 32, "languages":["Python", "javaScript", "C#"], "website": "none"}

json.dump(json_test, json_file, indent=2)

json_file.close()

'''
with open("Intermediate/my_file.json") as my_other_file:
  for json_line in my_other_file:
    print(json_line)
'''
json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict["name"])
print(type(json_dict))

# Fichero .csv

import csv

csv_file = open("Intermediate/my_file.csv", "w+", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "Age", "Language"])
csv_writer.writerow(["Diego", "Chiapa", 32, "Python"])
csv_writer.writerow(["Roswell", "", 2, "Cobol"])
csv_file.close()

csv_file = open("Intermediate/my_file.csv", "r+")
with open("Intermediate/my_file.csv") as my_other_file:
  for csv_row in my_other_file:
    print(csv_row)

# Fichero .xlsx
#import xlsx

# Fichero .xml
#import xml