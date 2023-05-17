#Altere o programa anterior fazendo com que todas as operações matemáticas sejam realizadas por uma única função. Todas as funcionalidades devem ser mantidas.

def opmatematica(n1, n2):
    if operacao == 1:
        return n1 + n2
    elif operacao == 2:
        return n1 - n2
    elif operacao == 3:
        return n1 * n2
    elif operacao == 4:
        return n1 / n2
    else:
        print('Operação inválida')
    

while True:
    print('\n1.Soma')
    print('2.Subtração')
    print('3.Multiplicação')
    print('4.Divisão')
    print('5.Finalizar o programa')
    operacao=int(input('Selecione a operação desejada: '))

    if operacao == 5:
        print('Fim do programa')
        break

    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))

    if operacao == 1:
        print('O resultado da soma é ', opmatematica(n1, n2))
    elif operacao == 2:
        print('O resultado da subtração é ', opmatematica(n1, n2))
    elif operacao == 3:
        print('O resultadoo da multiplicação é ', opmatematica(n1, n2))
    elif operacao == 4:
        print('O resultado da divisão é ', opmatematica(n1, n2))
    else:
        print('Operação invalida')