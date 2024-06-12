# Operadores

# Operadores Aritméticos
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # Modulo
print(10 // 3) # División entera
print(2 ** 3) # Exponente

print("Hola" + "Python") # Concatenar cadenas de texto
print("Hola" * 3) # repite el string la cantidad de veces

# Operadores Comparativos
print(3 > 4)
print(3 < 4) 
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# En el caso de los strings comparara la ordenación alfabética por ASCII
print("hola" > "python")
print("hola" < "python") 
print("hola" >= "bola")
print("hola" <= "python")
print("hola" == "hola")
print("hola" != "python")

# Operadores Lógicos
print(3 > 4 and "hola" > "python") # una proposición falsa Y otra proposición falsa = falso
print(3 > 4 or "hola" > "python") # una proposición falsa O otra proposición falsa = falso
print(3 < 4 and "hola" < "python") # una proposición verdadera Y otra proposición verdadera = verdadero
print(3 < 4 or "hola" > "python") # una proposición verdadera O otra proposición falsa = verdadero
print(3 < 4 or ("hola" > "python" and 4==4)) # una proposición verdadera O cualquier resultado de otra comparación = verdadero
print(not(3 > 4)) # Not: niega el estado de algo, en este caso una comparación 