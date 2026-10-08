x = 10
if x > 5:
    print("x es mayor que 5")

x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5")


x = 10
if x < 5:
    print("x es menor que 5")
elif x == 10:
    print("x es igual a 10")
else:
    print("x es mayor que 5 pero diferente de 10")

x=0
total=0
while x<10:
    nota=int(input("Ingrese la nota: "))
    if nota>6:
        total=total+1
        x=x+1
    print("Han aprobado ",total)

suma=0
for x in range(5):
    num=int(input("Ingrese un valor:"))
    suma=suma+num

promedio=suma/5
print("La suma es: ")
print(suma)
print("El promedio es: ")
print(promedio)