#Regular expressions
import re

minha_string = 'o gato, a gata, os gatinhos, os gatões'
#O primeiro parâmetro é o padrão que vou procurar, o segundo é minha string.
#O r transforma a string que está lá dentro em raw_string
# padrao = re.search(r'gato', minha_string)

#Utilizamos o \w para achar o número de letras em cada frase, se colocarmos 4 \w ele procura palavras com 4 letras.
# padrao = re.search(r'\w\w\w\w\w\w', minha_string)
padrao = re.findall(r'gat\w', minha_string)
if padrao :
    # print(padrao.group())
    print(padrao)
else:
    print("Padrão não encontrado!")