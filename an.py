# Escribir una función que calcule si el número ingresado es primo o no. Devolviendo True o False.


def calcPrimaridad():
    num = int(input("Ingrese un numero.\n"))
    cont = 0
    for i in range(1, num):
        if num % i == 0:
            cont += + 1
    if cont > 2: 
            print(f'{num} no es primo.')
    else:
            print(f'{num} es primo.')

calcPrimaridad()