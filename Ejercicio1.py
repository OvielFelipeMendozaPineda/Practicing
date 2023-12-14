
import random

numArray = []
def isNum(flag):

        n = int(input("Digite cantidad de números para la lista.\n"))
        if 0 < n < 11:
            for i in range(n):
                numArray.append(random.randint(1, 10))
        else:
            print("Entrada inválida.")
        print(sorted(numArray))
        print(sorted(numArray, reverse=True))

flag = True
while(flag):
    try:
        isNum(flag)
    except:
        print("Entrada inválida.")
