# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.

import random

vetor1 = []
vetor2 = []
vetor3 = []
for numero in range(10):
    v1 = random.randint(1, 100)
    vetor1.append(v1)
    vetor3.append(v1)

    v2 = random.randint(1, 100)
    vetor2.append(v2)
    vetor3.append(v2)

print(f'{vetor1}')
print(f'{vetor2}')
print(f'{vetor3}')