# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas

nome=str(input('Informe o nome: '))
nome=nome.upper()[::-1]
print(nome)