from math import floor
import numpy as np
import heapq as hp
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
    trocou = False
    for j in range(0, len(lista) - i - 1):
      if lista[j] > lista[j + 1]:
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp
        trocou = True
    if not trocou:
      break
   
def ordena_bubbleSort(lista, tamanho):
    resultado = []
    maior = 0
    index = 0
    for i in range(len(lista)):
        bubble_sort(lista[i])
    for i in range(tamanho):
        for j in range(len(lista)):
            if(lista[j] == []):
                continue
            if(maior < lista[j][-1]):
                maior = lista[j][-1]
                index = j
        maior = 0
        if(lista[index] != []):
            resultado.append(lista[index].pop())
    resultado.reverse()
    return resultado



def ordena_heap(lista,tamanho):
    maior = 0
    index = 0
    resultado = []
    #hp._heapify_max(resultado)
    for i in range(len(lista)):
        hp._heapify_max(lista[i])
    for i in range(tamanho):
        for j in range(len(lista)):
            if(lista[j] == []):
                continue
            elif(maior < lista[j][0]):
                maior = lista[j][0]
                index = j
        if(lista[index] == []):
            continue
        hp._heappop_max(lista[index])
        #hp.heappush(resultado, maior)
        resultado.append(maior)
        maior = 0
    #hp._heapify_max(resultado)
    resultado.reverse()
    return resultado


 
if __name__ == '__main__':
    entrada = [4, 6, 1, 19, 125, 5968, 26, 760, 16, 2, 3, 4, 3]
    entrada_random = random.sample(range(0,1000000), 1000000)
    #print(entrada)
    tamanho = len(entrada_random)

		
    start = time.time()
    partes = listAllocation(entrada_random, tamanho)
    resultado = ordena_heap(partes, tamanho)
    end = time.time()
    #print(resultado)
    print(end - start)