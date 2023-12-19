arrayNums= []
arrayNums2= []
limMáx = int(input("Ingrese el limite para su busqueda.\n"))

def isNumPrim(n):
    for i in range(10, n):
        if n % i == 0 :
            return False
    return n

def makeArray(arrayNums, limMáx):
    for i in range(10 , limMáx+1):
        res = isNumPrim(i)
        if res is not False:
            arrayNums.append(res)

    Palindrom(arrayNums)

def Palindrom(arrayNums):
    for i in range(len(arrayNums)):
        temp = str(arrayNums[i])
        invertido = temp[::-1]
        if  invertido == temp:
            arrayNums2.append(int(invertido))
    print(arrayNums2)
makeArray(arrayNums, limMáx)