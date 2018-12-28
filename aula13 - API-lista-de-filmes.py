import requests, json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t='+titulo+'&apikey=b7d5c054')
        dicionario = json.loads(req.text)
        return dicionario
    except Exception as err:
        print('Erro na conexão')
        return None

sair = False

def printar_detalhes(filme):
    print('Título: ', filme['Title'])
    print('Diretor: ', filme['Director'])
    print('Atores: ', filme['Actors'])
    print('Ano: ', filme['Year'])
    print('Nota: ', filme['imdbRating'])

while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado!')
        else:
            printar_detalhes(filme)
