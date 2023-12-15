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
cantPagada = 0 
coin10 = 0
coin50 = 0
change = 0
diff = 0
# Funcion para mostrar los productos
def showArrayProducts(flag):
    global cont
    print("Ingrese un número.")
    for i in arrayProducts[0]:
        print(f'\t{cont}. {i}')
        cont = cont + 1
# Funcion para carlcular el vuelto
def checkoutPayment (opcUser,cantPagada,arrayProducts,arrayCoins):
        global cantCoins10, cantCoins50, cantCoins100, diff, coin50, change, coin10
        print(f'Precio a pagar es de: ${arrayProducts[1][opcUser - 1]}.')
        while (cantPagada < arrayProducts[1][opcUser - 1]):
            cont = 1
            print("Ingrese moneda.")
            for i in range(len(arrayCoins)):
                print(f'\t{cont}. {arrayCoins[i]}')
                cont = cont + 1
            try:
                coins = int(input("\n"))
            except ValueError:
                print("Entrada inválida.")
                continue
            if coins == 1:
                cantCoins10 = cantCoins10 + 10
            elif coins == 2:
                cantCoins50 = cantCoins50 + 50
            elif coins == 3:
                cantCoins100 = cantCoins100 + 100
            cantPagada = cantCoins10 + cantCoins50 + cantCoins100
            print(f'Usted lleva ingresado: ${cantPagada}')
            if cantPagada >= (arrayProducts[1][opcUser - 1]):
                diff = cantPagada - arrayProducts[1][opcUser - 1]
                coin50 = trunc(diff / 50)
                change = diff % 50
                coin10 = trunc(change / 10) 
                print(f'Su vuelto es de: ${diff}\n $50x{coin50}\n $10x{coin10}')
# AlgortimoPrincipal
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
checkoutPayment (opcUser,cantPagada,arrayProducts,arrayCoins,)
if diff == 0:
    print("No hay vuelto.")



    