import requests

def retorana_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    print(response.json())
    dado_cep = response.json()
    print(dado_cep['logradouro'])
    print(dado_cep['complemento'])
    return dado_cep

def  retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    retorana_cep('58824000')
    #response = retorna_response('https://globallabs.academy/')