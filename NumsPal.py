import random
n = int(input("Ingrese el limite para la busqueda.\n"))
rango = n-10
arrayNum = []
for i in range(rango):
  arrayNum.append(random.randint(10,n))

arrayNum.sort()
print(arrayNum)