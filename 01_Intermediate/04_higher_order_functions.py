# funciones de orden superior

from functools import reduce

def sum_one(value):
  return value + 1

def sum_five(value):
  return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
  return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

# Closures

def sum_ten(original_value):
  def add(value): 
    return value + 10 + original_value
  return add

add_closure = sum_ten(5)
print(add_closure(5))

print((sum_ten(5))(1))

# Funciones de orden superior del sistema

numbers = [2, 5, 10, 21, 3, 30]

def multiply_two(number):
  return number * 2

def filter_greater_that_ten(number):
  return number > 10

def sum_two_values(first_value, second_value):
  return first_value + second_value

# Map
new_numbers = list(map(multiply_two, numbers))
print(new_numbers)
new_numbers = list(map(lambda number: number * 2, numbers))
print(new_numbers)

# Filter
numbers_greaters_that_ten = list(filter(filter_greater_that_ten, numbers))
print(numbers_greaters_that_ten)
numbers_greaters_that_ten = list(filter(lambda number: number > 10, numbers))
print(numbers_greaters_that_ten)

# Reduce
total = reduce(sum_two_values, numbers)
print(total)
total = reduce(lambda first_value, second_value: first_value + second_value, numbers)
print(total)



