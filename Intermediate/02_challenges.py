# Retos de programación

'''
#1 el famoso "fizz buzz"
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

    
fibonacci()