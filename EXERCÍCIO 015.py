print('DESAFIO 015')

print('∞'*11)
print()

print('›'*70)
print()

print('Escreva um programa que pergunte a quantidade de Km percorridos por um \n carro alugado e a quantidade de dias pelos quais ele foi alugado. \n Calcule o preço a pagar, sabendo que o carro custa R$60 por dia \n e R$0.15 por Km rodado.')

print()
print('›'*70)

print('Digite quantos dias, e quantos Km você andou de carro e eu vou calcular \n o dinheiro que você gastou.')

print()

dia=int(input('Quantos dias você andou? '))

km=float(input('Quantos Km você andou? '))

km2=0.15*km

dia2=60*dia

total=dia2+km2

print('›'*70)
print()

print('Você gastou R$ {:.0f} andando de carro.'.format(total))

print()
print('›'*70)