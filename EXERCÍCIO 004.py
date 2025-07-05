print ('>>>DESAFIO 004<<<')

print('—'*70)

print('Faça um programa que leia algo pelo teclado e mostre na tela\n o seu tipo primitivo e todas as informações possíveis sobre ele.')

print('—'*70)

n1 = input('Digite algo: ')

print()

print('Tipo primitivo:', type(n1))

print()

print('Tem letras?', n1.isalpha())

print('Tem dígitos?', n1.isdigit())

print('Tem números?', n1.isnumeric())

print('É decimal?', n1.isdecimal())

print('Tem letras ou números?', n1.isalnum())

print('Tem espaços?', n1.isspace())

print('Letras minúsculas?', n1.islower())

print('Letras maiúsculas?', n1.isupper())

print('Começa maiúsculo?', n1.istitle())

print('É uma variável?', n1. isidentifier())

print('É imprimível?', n1. isprintable())

print('Sem acento ou emoji?', n1.isascii())
