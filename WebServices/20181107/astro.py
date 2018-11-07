#!/usr/bin/env python3 
import cgi
import json
import requests
form = cgi.FieldStorage()
chave = "fdc40b93168b4f5ebcf214040180711"
cidade = form.getvalue("cidade")
consulta = "http://api.worldweatheronline.com/premium/v1/astronomy.ashx?q={}&key={}&format=json".format(cidade,chave)
resposta = requests.get(consulta)
informacoes = json.loads(resposta.content.decode('utf-8'))
print ("Content-type: text/html\n\n" )
print ("<html><body>")
print ("<h1>Nascer do Sol em {}</h1>".format(informacoes["data"]["request"][0]["query"]))
print ("<h2>{}</h2>".format(informacoes["data"]["time_zone"][0]["sunrise"]))
print ("<h1>Por do Sol em {}</h1>".format(informacoes["data"]["request"][0]["query"]))
print ("<h2>{}</h2>".format(informacoes["data"]["time_zone"][0]["sunset"]))
#print ("<br>O resultado eh {0:.2f}".format(resultado))
print ("</body></html>")
