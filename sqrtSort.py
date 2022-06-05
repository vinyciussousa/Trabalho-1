from math import floor
import scipy as sp
import numpy as np
import random

entrada = [4, 6, 1, 19, 125, 5968, 26, 760, 16, 2, 3, 4, 3]
tamanho = len(entrada)

print(tamanho)

partes = []
partesAux = []

#Do some black magic
tam_parte = round(np.sqrt(tamanho))
j = 0
for i in range(len(entrada)):
    if j < tam_parte:
        partesAux.append(entrada[i])
        j+=1
    elif j == tam_parte:
        partes.append(partesAux)
        partesAux = []
        partesAux.append(entrada[i])
        j = 1
partes.append(partesAux)

#print(partes)
#print(round(np.sqrt(tamanho))) # Tamanho das partes
#print((tamanho % floor(np.sqrt(tamanho)))) # Tamanho da última parte

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def ordena_bubbleSort(lista):
    resultado = []
    maiores = []
    index = 0
    for i in range(len(lista)):
        bubble_sort(lista[i])
    for i in range(len(lista)):
        maiores.append((lista[i][-1], i))
    for i in range(tamanho):
        bubble_sort(maiores)
        index = maiores[-1][1]
        maiores.pop()
        resultado.append(lista[index].pop())
        if(lista[index] == []):
            continue
        maiores.append((lista[index][-1], index))
    resultado.reverse()
    return resultado
    


#teste = partes[0].pop()
#print(partes[0])
resultado = ordena_bubbleSort(partes)
print(resultado)
#print(partes)

## entrada = [4, 6, 1, 19, 125, 5968, 26, 760, 16, 2] 
## partes = [[4,6,1],[19,125,5968],[26,760,16],[2]]