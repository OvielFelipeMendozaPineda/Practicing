# Escribe un programa que solicite al usuario ingresar su edad y luego determine si es mayor de edad o
# no utilizando una declaración if. Si la edad es mayor o igual a 18, muestra el mensaje "Eres mayor de
# edad", de lo contrario, muestra el mensaje "Eres menor de edad".


flag = True

def ageCal():
    Age = int(input("Ingrese su edad.\n"))
    if Age <= 0:
        print("Numero incorrecto.")
        ageCal()
    else:
        if Age >= 18:
            print("Usted es mayor de edad.")
        else:
            print("Usted es menor de edad.")
while(flag):
    try:
        ageCal()
        flag = False
    except:
        print("Intente nuevamente.")