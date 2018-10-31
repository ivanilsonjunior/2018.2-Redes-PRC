import json
import requests
from cryptography.fernet import Fernet



def recuperarChave(arquivo):
    return open(arquivo, 'r').read().encode('utf-8')

def recuperaSenha(arquivo):
    cipher_suite = Fernet(recuperarChave("chave.txt"))
    return cipher_suite.decrypt(open(arquivo, 'r').read().encode('utf-8')).decode('utf-8')

urls = { "token":"https://suap.ifrn.edu.br/api/v2/autenticacao/token/",
         "dados":"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"}

autenticacao = {
    "username": "2568824",
    "password": "{}".format(recuperaSenha("senha.txt"))
}

def getToken():
    response = requests.post(urls['token'], data=autenticacao)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['token']
    return None

cabecalho={'Authorization': 'JWT {0}'.format(getToken())}

def getInformacoes():
    response = requests.get(urls['dados'], headers=cabecalho)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None

informacoes = json.loads(getInformacoes())
# Para ver o conteudo de informacoes, descomente a linha abaixo
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#print (informacoes)
print ("Matricula: {0}\n\tNome: {1}\n\tE-Mail: {2}".format(informacoes['matricula'], informacoes['nome_usual'], informacoes['email']))
