quantidade_pessoas = int(input('Digite a quantidade de convidados que serão convidados para a festa: '))
lista_nomes = []
i = 0

while i < quantidade_pessoas:
    lista_nomes.append(input('Digite o nome do' + ' convidado ' + str(i) + ':'))
    i += 1

for nome in lista_nomes:
    print(nome)