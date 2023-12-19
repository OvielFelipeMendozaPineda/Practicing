arrayNums= []
arrayNums2= []
limMáx = int(input("Ingrese el limite para su busqueda."))

def isNumPrim(n):
    for i in range(2, n):
        if n % i == 0 :
            return False
    return n

def makeArray(arrayNums, limMáx):
    for i in range(2 , limMáx+1):
        res = isNumPrim(i)
        if res is not False:
            arrayNums.append(res)
    print(arrayNums)
    numPrimGem(arrayNums)

def numPrimGem(arrayNums):
    for i in range(len(arrayNums)-1):
        if arrayNums[i+1] - arrayNums[i] == 2:
            arrayNums2.append((arrayNums[i] , arrayNums[i+1]))
    print(arrayNums2)

makeArray(arrayNums, limMáx)