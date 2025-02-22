import random

print('DESAFIO 020')

print('›'*11)
print()

print('»'*70)
print()

print('O mesmo professor do desafio anterior quer sortear a ordem de\n apresentação de trabalhos dos alunos. Faça um programa\n que leia o nome dos quatro alunos e mostre a ordem sorteada.')

print()
print('»'*70)

print('Digite quatro coisas para eu sortear a sua ordem.')

print()

n1=str(input('Primeiro: '))

n2=str(input('Segundo: '))

n3=str(input('Terceiro: '))

n4=str(input('Quarto: '))

lista=[n1 , n2 , n3 , n4]

random.shuffle(lista)

print('»'*70)

print('A ordem será:\n {}'.format(lista))

print('»'*70)