# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista ÍMPAR. Imprima as três listas.

import random

sorteio = []
for i in range(20):
    sorteio.append(random.randint(1, 100))

par = []
impar = []
for numero in sorteio:
    if numero %2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Números sorteados:{sorteio}")
print(f"Os números ímpares são:{impar}")
print(f"Os números pares são:{par}")