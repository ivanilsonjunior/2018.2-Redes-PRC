import sys, time
from socket import *



if len(sys.argv) != 3:
    print ("Uso: {} porta Mensagem".format(sys.argv[0]))
    exit()

porta = 50000+int(sys.argv[1])
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

dados = sys.argv[2] 
s.sendto(dados.encode('utf-8'), ('<broadcast>', porta))
