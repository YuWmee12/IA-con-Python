#creacion de una lista de diferentes tipos
numeros=[1,2,3,4,5]
frutas=['manzana', 'banana', 'cereza']
mixta=[10, 'hola', 3.14, True]
vacia=[]
# Así se muestra la funcion que use  para imprir algo especifico de una lista
print(numeros[2]) #imprime el tercer elemento de la lista numeros
print(frutas[0]) #imprime el primer elemento de la lista frutas
print(mixta[-1]) #imprime el último elemento de la lista mixta
#Funciones que utilice para agregar datos a las listas

# Agregar al final
frutas.append('naranja') 

#insertar en una posición específica
frutas.insert(1, 'kiwi')

print(frutas) #imprime la lista frutas con los nuevos elementos agregados
frutas.remove('banana') #elimina el elemento 'banana' de la lista frutas
ultimo_elemento = numeros.pop()
del numeros[1] #elimina el segundo elemento de la lista numeros

print(frutas) 
print(numeros)

# Ciclos para solo recorrer una lista

# Usando un bucle for
for fruta in frutas:
    print(fruta)

# Usando un índice
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

# Operaciones utiles

print(len(frutas))     # Longitud de la lista
print(min(numeros))    # Mínimo valor
print(max(numeros))    # Máximo valor
print(sum(numeros))    # Suma de los valores
print(numeros[::-1])   # Invertir la lista