from math import sin, cos, tan, radians

print('DESAFIO 018')

print('«'*11)
print()

print('«'*70)
print()

print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor\n do seno, casseno e tangente desse ângulo.')

print()
print('«'*70)

print('Escreva um ângulo para eu mostrar seu seno, casseno e tangente.')

print()

ângulo=float(input('Digite o ângulo: '))

print('«'*70)

se=sin(radians(ângulo))

ca=cos(radians(ângulo))

ta=tan(radians(ângulo))

print('O seu seno é: {:.2f}'.format(se))

print('O seu casseno é: {:.2f}'.format(ca))

print('O seu tangente é: {:.2f}'.format(ta))

print('«'*70)