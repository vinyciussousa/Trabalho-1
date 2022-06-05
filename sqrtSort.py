from math import floor
import scipy as sp
import numpy as np
import random
import time

#Do some black magic
def listAllocation(lista, tamanho):
    partes = []
    partesAux = []
    tam_parte = round(np.sqrt(tamanho))
    j = 0
    for i in range(len(lista)):
        if j < tam_parte:
            partesAux.append(lista[i])
            j+=1
        elif j == tam_parte:
            partes.append(partesAux)
            partesAux = []
            partesAux.append(lista[i])
            j = 1
    partes.append(partesAux)
    return partes

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def ordena_bubbleSort(lista, tamanho):
    resultado = []
    maiores = []
    index = 0
    for i in range(len(lista)):
        bubble_sort(lista[i])
        maiores.append((lista[i][-1], i))
    for i in range(tamanho):
        bubble_sort(maiores) #the dark one
        index = maiores[-1][1]
        maiores.pop()
        resultado.append(lista[index].pop())
        if(lista[index] == []):
            continue
        maiores.append((lista[index][-1], index))
    resultado.reverse()
    return resultado

if __name__ == '__main__':
    entrada = [4, 6, 1, 19, 125, 5968, 26, 760, 16, 2, 3, 4, 3]
    entrada_random = random.sample(range(0,100000), 100000)
    #print(entrada_random)
    tamanho = len(entrada_random)

    start = time.time()
    partes = listAllocation(entrada_random, tamanho)
    resultado = ordena_bubbleSort(partes, tamanho)
    end = time.time()
    print(resultado)
    print(end - start)

#print(round(np.sqrt(tamanho))) # Tamanho das partes
#print((tamanho % floor(np.sqrt(tamanho)))) # Tamanho da última parte
## entrada = [4, 6, 1, 19, 125, 5968, 26, 760, 16, 2]
## partes = [[4,6,1],[19,125,5968],[26,760,16],[2]]