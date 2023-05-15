# Faça um programa que leia uma palavra fornecida pelo usuário e troque todas as vogais por “*”. Obs.: use while e concatenação.

palavra=(input('Informe uma palavra: '))
x = 0

troca = ''
while x < len(palavra):
    if palavra[x] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[x]
    x += 1
print(f'Nova palavra {troca}')
