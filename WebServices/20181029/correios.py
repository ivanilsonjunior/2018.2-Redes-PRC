import json
import requests

def getInformacoes(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None

resultado = json.loads(getInformacoes(59070400))
# Para ver o conteudo de informacoes, descomente a linha abaixo
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#print (resultado)
print ("CEP: {0}\n\tRua: {1}\n\tBairro: {2} Cidade/Estado:{3}/{4}".format(resultado['cep'], resultado['logradouro'], resultado['bairro'], resultado['localidade'], resultado['uf']))
