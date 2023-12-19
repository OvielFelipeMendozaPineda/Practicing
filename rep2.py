# Escribir una función que calcule el área de un cuadrado y otra que calcule el volumen de un cubo usando la primera función.

lado = 3
def areaCuadrado(lado):
  areaDelCuadrado= lado**2
  return areaDelCuadrado
def volCubo(lado):
  volCubo = lado*areaCuadrado(lado)
  return volCubo
print(areaCuadrado(lado))
print(volCubo(lado))