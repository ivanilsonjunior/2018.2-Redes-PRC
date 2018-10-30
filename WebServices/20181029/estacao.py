import json
import requests

def getInformacoes():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None

resultado = json.loads(getInformacoes())
lat = resultado['iss_position']['latitude']
log = resultado['iss_position']['longitude']
# Para ver o conteudo de informacoes, descomente a linha abaixo
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#print (resultado)
print("Latitude: {}\nLongitude: {}".format(lat, log))
print ("\nhttps://www.google.com/maps/search/?api=1&query={},{}".format(lat, log))
#print obj['timestamp']
#print obj['iss_position']['latitude'], obj['data']['iss_position']['latitude']
#print ("CEP: {0}\n\tRua: {1}\n\tBairro: {2} Cidade/Estado:{3}/{4}".format(resultado['cep'], resultado['logradouro'], resultado['bairro'], resultado['localidade'], resultado['uf']))
