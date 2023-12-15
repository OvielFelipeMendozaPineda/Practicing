from math import trunc
arrayProducts = [['A','B','C'], [270, 340, 390]]
arrayCoins = [10,50,100]
cont = 1 
opcUser = 0
flag = True
coins = 0
cantCoins10 = 0
cantCoins50 = 0
cantCoins100 = 0
cantPagada1 = 0 
cantPagada2 = 0 
cantPagada3 = 0 
coin10 = 0
coin50 = 0
change = 0
diff = 0

def showArrayProducts(flag):
    global cont
    print("Ingrese un número.")
    for i in arrayProducts[0]:
        print(f'\t{cont}. {i}')
        cont = cont + 1

while(flag):
    showArrayProducts(flag)
    try:
        opcUser = int(input("\n"))
        if 0 < opcUser <= len(arrayProducts[0]):
            flag = False
        else:
            raise
    except:
        print("Elección inválida.")
    cont = 1

if opcUser == int(1):
    print(f'Precio a pagar es de ${arrayProducts[1][opcUser - 1]}')
    while (cantPagada1 < arrayProducts[1][opcUser - 1]):
        cont = 1
        print("Ingrese moneda")
        for i in range(len(arrayCoins)):
            print(f'\t{cont}. {arrayCoins[i]}')
            cont = cont + 1
        coins = int(input("\n"))
        if coins == 1:
            cantCoins10 = cantCoins10 + 10
        elif coins == 2:
            cantCoins50 = cantCoins50 + 50
        elif coins == 3:
            cantCoins100 = cantCoins100 + 100
        cantPagada1 = cantCoins10 + cantCoins50 + cantCoins100
        print(cantPagada1)
    if cantPagada1 >= (arrayProducts[1][opcUser - 1]):
        flag = False
if cantPagada1 > arrayProducts[1][opcUser - 1]:
    diff = cantPagada1 - arrayProducts[1][opcUser - 1]
    coin50 = trunc(diff / 50)
    change = diff % 50
    coin10 = trunc(change / 10) 
    print(f'Su vuelto es de:\n $50x{coin50}\n $10x{coin10}')

if opcUser == int(2):
    print(f'Precio a pagar es de ${arrayProducts[1][opcUser - 1]}')
    while (cantPagada2 < arrayProducts[1][opcUser - 1]):
        cont = 1
        print("Ingrese moneda")
        for i in range(len(arrayCoins)):
            print(f'\t{cont}. {arrayCoins[i]}')
            cont = cont + 1
        coins = int(input("\n"))
        if coins == 1:
            cantCoins10 = cantCoins10 + 10
        elif coins == 2:
            cantCoins50 = cantCoins50 + 50
        elif coins == 3:
            cantCoins100 = cantCoins100 + 100
        cantPagada2 = cantCoins10 + cantCoins50 + cantCoins100
        print(cantPagada2)
    if cantPagada2 >= (arrayProducts[1][opcUser - 1]):
        flag = False
if cantPagada2 > arrayProducts[1][opcUser - 1]:
    diff = cantPagada2 - arrayProducts[1][opcUser - 1]
    coin50 = trunc(diff / 50)
    change = diff % 50
    coin10 = trunc(change / 10) 
    print(f'Su vuelto es de:\n $50x{coin50}\n $10x{coin10}')


if opcUser == int(3):
    print(f'Precio a pagar es de ${arrayProducts[1][opcUser - 1]}')
    while (cantPagada3 < arrayProducts[1][opcUser - 1]):
        cont = 1
        print("Ingrese moneda")
        for i in range(len(arrayCoins)):
            print(f'\t{cont}. {arrayCoins[i]}')
            cont = cont + 1
        coins = int(input("\n"))
        if coins == 1:
            cantCoins10 = cantCoins10 + 10
        elif coins == 2:
            cantCoins50 = cantCoins50 + 50
        elif coins == 3:
            cantCoins100 = cantCoins100 + 100
        cantPagada3 = cantCoins10 + cantCoins50 + cantCoins100
        print(cantPagada3)
    if cantPagada3 >= (arrayProducts[1][opcUser - 1]):
        flag = False
if cantPagada3 > arrayProducts[1][opcUser - 1]:
    diff = cantPagada3 - arrayProducts[1][opcUser - 1]
    coin50 = trunc(diff / 50)
    change = diff % 50
    coin10 = trunc(change / 10) 
    print(f'Su vuelto es de:\n $50x{coin50}\n $10x{coin10}')

if diff == 0:
    print("No hay vuelto.")



    