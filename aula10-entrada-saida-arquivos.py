#Abre um arquivo chamado arquivo.txt, se passar o w ele cria se não existir
#O segundo parâmetro é o modo de abrir, se colocar w ele escreve, r ele lê
#o método a de append ele escreve ou criar arquivos, (adicionar)
#abrir arquivos que não são de texto, abre com modo b


# arquivo = open('arquivo.txt', 'w')
# for i in range(0, 1000):
#     arquivo.write(str(i) + '\n')

arquivo = open('arquivo.txt', 'r')

for linha in arquivo:
    print(linha)
