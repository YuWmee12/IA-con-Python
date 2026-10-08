#operadores logicos 
#operador and
print("\noperador and:")
print(True and True) 
print(True and False)
print(False and True)
print(False and False)

#operador or
print('\noperador or:')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

##combinacion de operadores 
print('\nejemplo combinado de operadores logicos')
print(True and True and False)
#evaluacion de paso a paso 
print(False and True or True or False)

#operador not
print("\noperador not:")
print(not True)
print(not False)
print(not not not not not True)

# not not not not True equivale a not (not (not (not True)))

# Uso de valores alternativos (1 y 0)
print("\nUso de valores alternativos:")
print(not 0)  # True
print(not 1)  # False