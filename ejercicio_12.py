# Ejercicio 1
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Ejercicio 2
for numero in range(1, 6):
    print(numero)

# Ejercicio 3
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Ejercicio 4
entrada = ""
while entrada != "python":
    entrada = input("Adivina la palabra secreta: ").lower()
    print("¡Correcto!")

# Ejercicio 5
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")

# Ejercicio 6
numeros = [1, 2, 3, 4, 5, 6]
for num in numeros:
    if num == 5:
        break
    print(num)

for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# Ejercicio 7
for letra in "Python":
    print(letra)
else:
    print("Bucle finalizado ✅")