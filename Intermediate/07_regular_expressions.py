# Expresiones regulares

import re

my_string = "Esta es la lección numero 7: Lección Expresiones regulares"
my_other_string = "Esta no es la lección numero 6: Lección Manejo de ficheros"

# Match
match = re.match("Esta es la lección", my_string)
span = match.span()


print(match)
print(span)
print(my_string[match.start():match.end()])


match = re.match("Esta no es la lección", my_other_string)
# if not(match == None):
# is match is not None:
if match != None:
  print(match)
  print(span)
  print(my_other_string[match.start():match.end()])

# Search
search = re.search("lección", my_string, re.I)
print(search)
print(my_string[search.start():search.end()])

# Findall
findall = re.findall("es", my_string)
print(findall)

# Split
split = re.split(" ", my_string)
print(split)

# Sub
sub = re.sub("a", "y", my_string)
print(sub)
sub = sub = re.sub("lección|Lección", "LECCIÓN", my_string)
print(sub)
sub = sub = re.sub("[L|l]ección", "LECCIÓN", my_string)
print(sub)

# Patrones
pattern = r"[Ll]ección"
print(re.findall(pattern, my_string))

pattern = r"[Ll]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))