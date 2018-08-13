import os
# Receive UDP packets transmitted by a broadcasting service

MYPORT = 5000

import sys
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', MYPORT))

data = ""
while data != "sair":
    data, wherefrom = s.recvfrom(1500, 0)
    print "Mensagem recebida de :", wherefrom
    if data == "sair":
        break
    os.system(data)
