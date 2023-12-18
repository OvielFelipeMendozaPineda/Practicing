star = '*'
numero = int(input("Ingrese un numero.\n"))
def starprint(star, numero):
    for _ in range(numero):
      print(star)
      star += "*"
starprint(star, numero)