minha_lista = ['Nathan', 'Igor', 'Woshinton'] #Lista (List)
#A tupla não é volátil como a lista.
minha_tupla = ('Nathan', 'Carlos', 'João') #Tupla (Tuple)
meu_dicionario = {'nome': 'Guilherme', 'idade': 27} #Dicionário (Dict)
meu_conjunto = {'Gui', 'João'} #Conjunto (Set)

for nome in minha_tupla:
    print(nome)

if 'Nathan' in minha_tupla:
    print('Nathan está na tupla')
if 'Guilherme' in meu_dicionario.values():
    print('Guilherme está no dicionario')