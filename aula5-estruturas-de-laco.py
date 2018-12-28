nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia', 'João']
nome = 'Nathan Carlos'


#Range cria uma lista de números.
#Cria um objeto com números até 5 como passei por parâmetro.
# lista_de_numeros = range(5)
# #De 5 até 10
# lista_de_numeros = range(5, 10)
# #De 0 até 100 pulando de 2 em 2.
# lista_de_numeros = range(0, 100, 2)
# for n in lista_de_numeros:
#     print(n)

#For também é utilizado como foreach no python.
#Para cada nome na lista de nomes ele printa.
# for nome in nomes:
#     print(nome)

# for i in range(len(nomes)):
#     print(nomes[i])
#     nomes.append('Oii')
# print(nomes)

#O for percorre uma coleção, tanto string quanto lista.

# for i in nome:
#     print(i)

# i = 0
# while i < 10:
#     print('i ainda é menor que 10', i)
#     i = i + 1
# print('Acabou o while', i)

# while True:
#     print('Loop infinito', i)
#     i = i + 1

lista_frutas = ['maca', 'pera', 'uva', 'abacaxi', 'morango']
#
# contador = 0
#
# for fruta in lista_frutas:
#     contador += 1
#
# print (contador)
# print (len(lista_frutas))
numero = 0
#Colocamos break para sair de um estrutura de repetição.
while True:
    print(numero)
    if numero == 20:
        break;
    numero += 1
