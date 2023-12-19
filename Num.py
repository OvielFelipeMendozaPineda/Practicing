#Escribir un programa que solicite al usuario ingresar un número entero y determine si es positivo,
#negativo o cero. Imprimir un mensaje correspondiente para cada caso.

import time
flag = True
def smash():
    n = (input("Ingrese un numero.\n"))
    if n > 0: 
        print(f'El numero {n} es positivo')
    elif n < 0:
        print(f'El numero {n} es negativo')
    else:
        print(f'El numero {n} es igual al 0')


   
while(flag):
    try:
        smash()
        flag = False
    except: ValueError
    print("Lo sentimos. Ha ocurrdio un error. Vuelva a intentar.")
    time.sleep(1)
    
