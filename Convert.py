farenheit = 0 
celsius = 0
def convertCelsiusFaren():
    celsius = float(input("Ingrese temperatura en grados celsius.\n"))
    farenheit = ((celsius*9/5) + 32) 
    return farenheit

def convertFarenCelsius():
    farenheit = float(input("Ingrese temperatura en grados Farenheit.\n"))

    celsius = ((farenheit-32) * 5/9)
    return celsius

print(f'la temperatura en grados Farenheit es de {convertCelsiusFaren()}')
print(f'la temperatura en grados Farenheit es de {convertFarenCelsius()}')