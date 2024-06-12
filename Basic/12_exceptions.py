# Manejo de excepciones

numberOne = 5
numberTwo = 1

numberTwo = "1"

#try except
try:
  # Bloque de código que va a intentar ejecutar
  print(numberOne + numberTwo)
  print("No se ha producido un error.")
except:
  # Se ejecuta si se produce una excepción
  print("Se ha producido un error.")

#try except else
try:
  # Bloque de código que va a intentar ejecutar
  print(numberOne + numberTwo)
  print("No se ha producido un error.")
except:
  # Se ejecuta si se produce una excepción
  print("Se ha producido un error.")
else:
  # Se ejecuta si no se produce una excepción
  print("La ejecución continua correctamente.")

#try except else finally
try:
  # Bloque de código que va a intentar ejecutar
  print(numberOne + numberTwo)
  print("No se ha producido un error.")
except:
  # Se ejecuta si se produce una excepción
  print("Se ha producido un error.")
else:
  # Se ejecuta si no se produce una excepción
  print("La ejecución continua correctamente.")
finally:
  # Se ejecuta siempre
  print("La ejecución continua.")

# Excepciones por tipo
try:
  print(numberOne + numberTwo)
  print("No se ha producido un error.")
except TypeError:
  # Se ejecuta si se produce una excepción de tipo
  print("Se ha producido un error de tipo.")
  if type(numberOne) != int and type(numberOne) != float:
     numberOne = int(numberOne)
  elif type(numberTwo) != int and type(numberTwo) != float:
    numberTwo = int(numberTwo)
  numberOne = int(numberOne)
  print(numberOne + numberTwo)
  print("Se ha solucionado un error.")
else:
  print("La ejecución continua correctamente.")
finally:
  print("La ejecución continua.")


numberTwo = "1"
# Captura la información de la excepción
try:
  print(numberOne + numberTwo)
except Exception as e:
  print(e)