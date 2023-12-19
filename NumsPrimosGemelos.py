import random

arrayNumsPrimos = []
arrayNums = []


n = int(input("Ingrese limite superior del rango.\n"))
# Establecemos el primer arreglo
for i in range(2,n):
  arrayNums.append(random.randint(2,n))
# Se ordena 
arrayNums.sort()
print(arrayNums)

#Se establece el arreglo con los numeros primos

for i in range(len(arrayNums)):
  cont = 0 
  for j in range(1, arrayNums[i]):
    if arrayNums[i] % j == 0:
        cont += + 1      
  if cont > 2:
    print("no es primo.")
  else:
    arrayNumsPrimos.append(arrayNums[i])
print(arrayNumsPrimos)















