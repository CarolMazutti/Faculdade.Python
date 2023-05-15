# Peça para o usuário digitar uma palavra e verifique se ela é palíndrome. Um palíndromo é uma palavra, frase ou qualquer outra sequência de unidades que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita.

palavra=str(input('Digite uma palavra: '))
if palavra == palavra[::-1]:
    print(f'A palavra {palavra} é palíndrome')
else:
    print(f'A palavra {palavra} não é palíndrome')