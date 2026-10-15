# Creación de la variable vacía del conjunto 1
Conjunto1 = set()

# Asignación del conjunto a la variable
Conjunto1 = {1, 2, 3, 4, "Hola.", 3.14}

# Creación de la variable vacía del conjunto 2
Conjunto2 = set()

# Asignación del conjunto a la variable
Conjunto2 = {9, 11, 15, "Buenas noches.", 6.022}

# Imprimir datos del conjunto
print("Estos datos contiene el conjunto 1: ", Conjunto1)
print("Estos datos contiene el conjunto 2: ", Conjunto2, "\n")

# Añadir más datos a un conjunto creado
Conjunto1.add(5)
Conjunto1.add(7)
Conjunto1.add("Soy un conjunto.")
Conjunto1.add(14.5)

# Imprimir datos del conjunto
print("Estos datos contiene el conjunto 1: ", Conjunto1)
print("Estos datos contiene el conjunto 2: ", Conjunto2, "\n")

# Eliminar datos de un conjunto
Conjunto1.discard(14.5)

print("Estos datos contiene el conjunto 1: ", Conjunto1)

# Limpiar un conjunto
Conjunto1.clear()
Conjunto2.clear()
print("Se limpió el conjunto 1 y 2.\n")

print("Estos datos contiene el conjunto 1: ", Conjunto1)
print("Estos datos contiene el conjunto 2: ", Conjunto2, "\n")

# Consultar si un elemento está en el conjunto
# Definir los conjuntos
Conjunto1 = {1, 2, 3, 4, 5, 8, 10}
Conjunto2 = {6, 7, 8, 9, 10, 12, 15}
print("Estos datos contiene el conjunto 1: ", Conjunto1)
print("Estos datos contiene el conjunto 2: ", Conjunto2, "\n")

# Pedir al usuario el valor a consultar
Consulta = input("Ingresa el valor que quieres consultar: ")

# Convertir la entrada a un número (opcional, si los conjuntos contienen números)
try:
    Consulta = int(Consulta)
except ValueError:
    print("Por favor, ingresa un número válido.")
    exit()

# Verificar si el valor está en Conjunto1
if Consulta in Conjunto1:
    print(f"El dato ingresado ({Consulta}) sí se encuentra en Conjunto1.\n")
else:
    print(f"El dato ingresado ({Consulta}) no se encuentra en Conjunto1.\n")

# Verificar si el valor está en Conjunto2
if Consulta in Conjunto2:
    print(f"El dato ingresado ({Consulta}) sí se encuentra en Conjunto2.\n")
else:
    print(f"El dato ingresado ({Consulta}) no se encuentra en Conjunto2.\n")

# Operaciones con conjuntos
union = Conjunto1 | Conjunto2  # Unión
interseccion = Conjunto1 & Conjunto2  # Intersección
diferencia = Conjunto1 - Conjunto2  # Diferencia
diferencia_simetrica = Conjunto1 ^ Conjunto2  # Diferencia simétrica

# Impresión de operaciones con conjuntos
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
print("Diferencia Simétrica:", diferencia_simetrica, "\n")

# Para qué se usa un conjunto
# Se usa para eliminar duplicados de una lista
lista = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7]
conjunto_sin_duplicados = set(lista)
print("Lista sin duplicados:", conjunto_sin_duplicados, "\n")

# Conversión entre tipos de datos
lista_desde_conjunto = list(Conjunto1)
tupla_desde_conjunto = tuple(Conjunto1)

print("Lista desde conjunto:", lista_desde_conjunto)
print("Tupla desde conjunto:", tupla_desde_conjunto, "\n")

# Uso de conjuntos en lógica matemática
# Operación para saber si un conjunto es subconjunto de otro
Conjunto_Original = {2, 4, 8, 10}
Conjunto_Padre = {2, 4, 6, 8, 10, 12, 15}
Conjunto_OriginalMenor = {2, 4, 6}
Conjunto_Disjunto = {3, 6, 9, 12}

# Impresión de los datos que contienen los conjuntos
print("Nombre de los conjuntos que se usarán en lógica matemática: ")
print("Conjunto_Original:", Conjunto_Original)
print("Conjunto_Padre: ", Conjunto_Padre)
print("Conjunto_OriginalMenor: ", Conjunto_OriginalMenor)
print("Conjunto_Disjunto: ", Conjunto_Disjunto, "\n")

# Operación para saber si un conjunto es hijo de otro más grande
es_subconjunto = Conjunto_Original.issubset(Conjunto_Padre)

# Operación para saber si un conjunto es padre de otro más pequeño
es_superset = Conjunto_Original.issuperset(Conjunto_OriginalMenor)

# Son 2 conjuntos disjuntos porque no comparten ningún elemento en común
es_disjunto = Conjunto_Original.isdisjoint(Conjunto_Disjunto)

print("¿Conjunto_Original es subconjunto o hijo de otro conjunto más grande?", es_subconjunto)
print("¿Conjunto_Original es superconjunto de Conjunto_OriginalMenor?", es_superset)
print("¿Conjunto_Original y Conjunto_Disjunto son disjuntos o no comparten ningún elemento en común?", es_disjunto, "\n")
