#  Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

s1=str(input('Informe a primeira string: '))
s2=str(input('Informe a segunda string: '))

print(f'String 1: {s1}')
print(len(s1))

print(f'String 2: {s2}')
print(len(s2))

if s1 == s2 and len(s1) == len(s2):
    print('As strings são iguais e possuem o mesmo comprimento')
elif s1 == s2:
    print('As strings são iguais')
elif len(s1) == len(s2):
    print('As strings são diferentes mas possuem o mesmo comprimento')
else:
    print('As strings são diferentes')