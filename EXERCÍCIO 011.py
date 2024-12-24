print('DESAFIO 011')

print(':'*11)
print()

print('-'*40)
print()

print('Faça um programa que leia a largura \ne a altura de uma parede em metros, \ncalcule a sua área e a quantidade \nde tinta necessário para pintá-lo, \nsabendo que cada litro de tinta \npinta uma área de 2m².')

print()
print('-'*40)
print()

print('Digite dois números largura e altura, \ne irei mostrar sua área e o quanto de \ntinta necessários sendo cada litro 2m².')

print()

lar1=int(input('Digite a largura: ' ))

print()

alt1=int(input('Digite a altura: '))

área=lar1*alt1

tinta=(lar1*alt1)/2

print()
print('-'*40)
print()

print('Para pintar a parede de {}m, \nvocê precisará de {} litros de tinta.'.format(área,tinta))