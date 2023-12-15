arrayDolar = []
day = 1
diff = 0
ran = 0
n = 0

def CalcRaise(flag):
    n = int(input("Ingrese cantidad de dias.\n"))
    for i in range(n):
        precio = int(input(f'Ingrese el precio. Dia {i+1}\n'))
        arrayDolar.append(precio)
    for i in range(n-1):
        diff = arrayDolar[i+1] - arrayDolar[i]
        if abs(diff) > abs(ran):
            ran = diff
            day = i + 1
    if ran != 0: 
        print(f'El mayor cambio sucedio del {day} al {day+1} con una diferencia de {abs(ran)} puntos.') 
    else:
        print("No hubo alza.")

flag = True
while(True):
    try:
        CalcRaise(flag)
        flag = False
    except:
        print("Entrada no válida.")