#Faça um programa que realize as operações de soma, subtração, multiplicação e divisão de forma que cada operação matemática esteja em uma função distinta (uma função para cada operação matemática). Os números devem ser obtidos fora da função, e passados como parâmetro para as demais funções. Cada função deve retornar o resultado para ser exibido fora delas. No início do programa deve ser apresentado um menu ao usuário pedindo qual operação matemática ele deseja fazer, ou se o usuário deseja finalizar o programa. O usuário pode realizar quantos operações forem necessárias. Caso seja digitado uma opção inválida o usuário deve ser informado e retornar ao menu de opções.

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

def menu():
    print('\n1.Soma')
    print('2.Subtração')
    print('3.Multiplicação')
    print('4.Divisão')
    print('5.Finalizar o programa')

def numeros():
    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))
    return n1, n2

while True:
    menu()
    operacao=int(input('Selecione a operação desejada: '))

    if operacao == 5:
        print('Fim do programa')
        break
    elif operacao == 1:
        n1, n2 = numeros()
        resultado = soma(n1, n2)
        print('O resultado da soma é ', resultado)
    elif operacao == 2:
        n1, n2 = numeros()
        resultado = sub(n1, n2)
        print('O resultado da subtração é ', resultado)
    elif operacao == 3:
        n1, n2 = numeros()
        resultado = mult(n1, n2)
        print('O resultadoo da multiplicação é ', resultado)
    elif operacao == 4:
        n1, n2 = numeros()
        resultado = divisao(n1, n2)
        print('O resultado da divisão é ', resultado)
    else:
        print('Operação invalida')
