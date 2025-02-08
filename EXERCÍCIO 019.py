import random

print('DESAFIO 019')

print('—'*11)
print()

print('—'*70)
print()

print('Um professor quer sortear um dos seus quatro alunos para apagar o\n quadro. Faça um programa que ajude ele, lendo o nome deles e\n escrevendo o nome do escolhido.')

print()
print('—'*70)

print('Digite quatro coisas para eu sortear.')

print()

n1=str(input('Primeiro: '))

n2=str(input('Segundo: '))

n3=str(input('Terceiro: '))

n4=str(input('Quarto: '))

lista=[n1, n2, n3, n4]

resposta=random.choice(lista)

print('—'*70)

print('O escolhido foi {}'.format(resposta))

print('—'*70)