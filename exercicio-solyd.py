idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Você está apto a entrar no exército!')
else:
    print('Você não está apto a entrar no exército!')