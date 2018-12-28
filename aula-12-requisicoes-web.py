import requests #Beautiful Soup 4 BS4 pip install bs4

header = {'Content-Type': 'application/json'}
meus_cookies = { 'Ultima-visita':'10-10-2020'}
dados = {
  "title": "atividade",
  "description": "atividade",
  "dataInicio": "2018-12-24",
  "dataFim": "2018-12-30"
}
try:
    # requisicao = requests.get('link', headers = header)
    requisicao = requests.post('link',
                               headers = header,
                               cookies=meus_cookies,
                               data=dados)
    print(requisicao.text)
except Exception as err:
    print('Ocorreu o seguinte erro ao processar requisição: ', err)


