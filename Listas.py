# estoEsUnaLista = ["Hola", 1,4,6, "Adios"]
# estoEsUnaLista2 = ["Manzana","Coco"]
# estoEsUnaLista.append('Esta funcion agrega a la lista en el ultimo indice')
# estoEsUnaLista.extend(estoEsUnaLista2)
# estoEsUnaLista.insert(3, "Inserte esto en la posicion 3")
# estoEsUnaLista.remove(4) #Elimina el primero igual al argumento que encuentre}
# valorDeLaLista = estoEsUnaLista.pop(7) #Si no pongo indice, elimina el ultimo de la lista
# print(estoEsUnaLista)
# print(valorDeLaLista)

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# arrayAsignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# arrayNotas = []
# for i in range(len(arrayAsignaturas)):
#   arrayNotas.append(input(f'ingrese nota de la asignatura {arrayAsignaturas[i]}.\n'))

# for i in range(len(arrayAsignaturas)):
#   print(f'En la asignatiura {arrayAsignaturas[i]}, obtuvo nota de: {arrayNotas[i]}.')

 # Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

import random

arrayNum = []
for i in range(10):
  arrayNum.append(random.randint(0,11))
arrayNum.sort(reverse=True)
print(','.join(arrayNum))