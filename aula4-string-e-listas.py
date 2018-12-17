#Listas e strings.
frase = 'Oi, tudo bem?'
lista_nomes = ['Nathan', 'Maria', 'Vitor', 'Rodrigo']
print(frase[0])
print(frase[0:13:1])
# Removendo nome da lista.
# lista_nomes.remove('Nathan')
# podemos definir de onde até onde ele irá imprimir os dados, por exemplo do 0 até o 3
print(lista_nomes[0:3])
# para imprimir o último eu coloco assim:
print(lista_nomes[-1])

#Adicionando nomes na lista com append.(Ele sempre insere no último lugar da lista)
lista_nomes.append('Marcio')
print(lista_nomes)
lista_nomes.remove('Rodrigo')
print(lista_nomes)
lista_nomes.insert(1, 'Matheus')
print(lista_nomes)
lista_nomes[0] = 'Roberval'
print(lista_nomes)
print(lista_nomes.count('Vitor'))
print(len(frase))
print(len(lista_nomes))
#O pop tira o último da lista e retorna o dado retirado.
print(lista_nomes.pop())
lista_nomes.clear()
print(lista_nomes)
print(frase.lower())
#Separa a frase.
print(frase.split(','))



