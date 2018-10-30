#!/usr/bin/env python3 
import cgi
import json
import requests

form = cgi.FieldStorage()
valor = form.getvalue("CEP")

def getInformacoes(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None

resultado = json.loads(getInformacoes(valor))
print ("Content-type: text/html\n\n")
print ("<html><body>")
print ("<h1>{}</h1>".format(resultado['cep']))
print ("<br>Rua: {}".format(resultado['logradouro']))
print ("<br>Bairro: {}".format(resultado['bairro']))
print ("<br>Cidade: {}".format(resultado['localidade']))
print ("</body></html>")
# Para ver o conteudo de informacoes, descomente a linha abaixo
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#print (resultado)
#print ("CEP: {0}\n\tRua: {1}\n\tBairro: {2} Cidade/Estado:{3}/{4}".format(resultado['cep'], #resultado['logradouro'], resultado['bairro'], resultado['localidade'], resultado['uf']))
