# Faça um programa solicite a data de nascimento (dd/mm/aaaa) e imprima com o nome do mês por extenso. Ex.: 01 de março de 2012.

data=(input('Informe a data: dd/mm/aaaa: '))

data=data.split('/')

dia=data[0]
mes=int(data[1])
ano=data[2]

meses = ['zero', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro']

print(f'{dia} de {meses[mes]} de {ano} ')