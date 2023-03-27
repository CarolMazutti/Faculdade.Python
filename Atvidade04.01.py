# Sorteie 10 inteiros entre 1 e 100 (a função randint pode facilitar o seu trabalho) para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.

import random

numeros = []
for i in range(10):
    numeros.append(random.randint(1, 100))

maior = numeros[0]
menor = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Números sorteados:{numeros}")
print(f"Maior valor:{maior}")
print(f"Menor valor:{menor}")