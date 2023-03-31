#Faça um programa que gere um vetor de 20 posições. Preencha esse vetor de acordo com a posição, colocando 1 na posição correspondente a um número par e 0 a um número ímpar. No final, imprima o vetor gerado.

import random

sorteio = []
for i in range(20):
    sorteio.append(random.randint(1, 100))
print(f'{sorteio}')

vetor = []
for i in sorteio:
    if i %2 == 0:
        i = 1
        vetor.append(i)
    else:
        i = 0
        vetor.append(i)
print(f'{vetor}')
