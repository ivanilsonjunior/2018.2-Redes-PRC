#!/usr/bin/env python3 
import cgi
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
#print("Latitude: {}\nLongitude: {}".format(lat, log))
print ("Content-type: text/html\n\n")
print ("<html><body>")
print ("<a href=\"https://www.google.com/maps/search/?api=1&query={},{}\">Local da Estação Espacial</a>".format(lat, log))
print ("</body></html>")


