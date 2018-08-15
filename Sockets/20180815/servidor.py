import os
import sys
# Receive UDP packets transmitted by a broadcasting service
porta = 50000+int(sys.argv[1])

import sys
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', porta))
print ("Abrindo porta {}".format(porta))

dados = ""
dados, origem = s.recvfrom(1500, 0)
print ("[{}]Mensagem recebida de {}: {}".format(porta, origem, dados.decode('utf-8')))
