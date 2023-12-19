from os import system
import time
num = int(input("Ingrese un numero entero\n"))
def facto(num):
  facto = 0
  if num == 1 or num ==0:
    return 1
  else:
    for _ in range(num):
      facto += num * num-1
  return facto
print(facto(num))
time.sleep(5)
system("clear")