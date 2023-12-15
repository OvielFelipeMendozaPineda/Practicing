arrayProducts = [['A','B','C'], [270, 340, 390]]
arrayCoins = [10,50,100]
opcUser = 0
flag = True
coins = 0
# Funcion para mostrar los productos
def showArrayProducts(flag):
    cont = 1 
    print("Ingrese un número.")
    for i in arrayProducts[0]:
        print(f'\t{cont}. {i}')
        cont = cont + 1
# Funcion para carlcular el vuelto
def checkoutPayment (opcUser,arrayProducts,arrayCoins):
        coin10 = coin50 = change = cantCoins10 = cantCoins50 = cantCoins100 = diff = 0
        print(f'Precio a pagar es de: ${arrayProducts[1][opcUser - 1]}.')
        cantPagada = 0 
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
                cantCoins10 += + 10
            elif coins == 2:
                cantCoins50 += + 50
            elif coins == 3:
                cantCoins100 += + 100
            cantPagada = cantCoins10 + cantCoins50 + cantCoins100
            print(f'Usted lleva ingresado: ${cantPagada}')
            if cantPagada >= (arrayProducts[1][opcUser - 1]):
                diff = cantPagada - arrayProducts[1][opcUser - 1]
                coin50 = diff // 50
                change = diff % 50
                coin10 = change // 10
                print(f'Su vuelto es de: ${diff}\n\t $50x {coin50}\n\t $10x {coin10}')
        return diff, cantPagada, coin10, coin50
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
diff, cantPagada, coin10, coin50 = checkoutPayment (opcUser,arrayProducts,arrayCoins,)
if diff == 0:
    print("No hay vuelto.")
    