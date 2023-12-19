import datetime
año = datetime.datetime.now().year
meses_30 = ['abril','junio','septiembre','noviembre']
meses_31 = ['enero','marzo','mayo','julio','agosto','octubre','diciembre']
flag = True
dias = None
def month():
    input_mes = str(input("Ingrese el nombre del mes.\n"))
    mes = input_mes.lower()
    if  mes in meses_30:
        print(f'el mes {mes} tiene 30.')
        return False
    if  mes in meses_31:
        print(f'el mes {mes} tiene 31.')
        return False
    if mes == 'febrero':
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            print(f'{mes} tiene 29')
        else:
            print(f'{mes} tiene 28')
    else:  
        print("Entrada inválida")
        return True
#def dayCalc():


while(flag):
    try:
        flag = month()
    except: 
        print("Ha ocurrido un error. Reintente.")


