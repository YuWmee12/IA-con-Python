#operadores de identidad

a=[1,2,3]
b=a
c=[1,2,3]

print(a is b)
print (a is c)
print(a == c)
print (a is not c)

a=['hola', 'como', 'hola']
b=a
c=['hola', 'como', 'hola']
# Definimos una lista y la asignamos a dos variables
A = ["chocolate", "vainilla"]
B = A  # B es la misma lista que A
C = ["chocolate", "vainilla","Fresa" ]  # C es una lista nueva con el mismo contenido

# Comparación con is
print(A is B)  # True -> A y B son el mismo objeto en memoria
print(A is C)  # False -> A y C tienen el mismo contenido, pero son objetos distintos

# Comparación con ==
print(A == C)  # True -> A y C tienen el mismo contenido
print(A is not C)  # True -> A y C no son el mismo objeto en memoria