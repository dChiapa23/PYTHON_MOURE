# Retos de programación

'''
#1
Escribe un programa que muestre por consola (con un print) los números de 1 a 100
(ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzbuzz():
    for n in range(1,101):
        if (n % 3) == 0 and (n % 5) == 0:
          print("fizzbuzz")
        elif (n % 3) == 0:
          print("fizz")
        elif (n % 5) == 0:
          print("buzz")
        else:
          print(f"{n}")
  
#fizzbuzz()

'''
#2
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(first_word, second_word):
  first_word = first_word.lower()
  second_word = second_word.lower()
  if len(first_word) == len(second_word) and first_word != second_word:
    for i in first_word:
      if first_word.count(i) == second_word.count(i):
        is_anagram = True
      else:
        is_anagram = False
  else:
    is_anagram = False
  return is_anagram

#print(is_anagram("tinta", "taNti"))

'''
#3
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
  first_value, second_value = 0, 1
  for i in range(0,50):
    print(first_value)
    next_value = first_value + second_value
    first_value = second_value
    second_value = next_value

    
#fibonacci()

'''
#4
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''


# 2,3,5,7,11,13
def is_prime(number):
  dividers = 0
  for d in range(1, number + 1):
    if number % d == 0:
      dividers += 1
  if dividers != 2:
    return False
  return True

def print_primes_numbers(start, end):
  for n in range(start, end):
    if is_prime(n):
      print(n)

#print_primes_numbers(1, 100)

'''
#7
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje
que lo hagan de forma automática. Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def reverse_text(text):
  new_text = ""
  text_len = len(text)
  for i in range(text_len):
    new_index = text_len - i - 1
    new_text += (text[new_index])
  return new_text

print(reverse_text("Hola mundo"))