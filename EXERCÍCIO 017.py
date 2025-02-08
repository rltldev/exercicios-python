from math import hypot

print('DESAFIO 017')

print('»'*11)
print()

print('»'*70)
print()

print('Faça um programa que leia o comprimento do cateto oposto e do cateto\n adjacente de um triângulo retângulo, calcule e mostre o comprimento\n da hipotenusa.')

print()
print('»'*70)

print('Escreva o cateto oposto e o cateto adjacente do triângulo, para eu\n medir a hipotenusa.')

print()

co=float(input('Digite o cateto oposto: '))

ca=float(input('Digite o cateto adjacente: '))

hi=hypot(ca,co)

print('»'*70)
print()

print('A hipotenusa é {:.2f}'.format(hi))

print()
print('»'*70)