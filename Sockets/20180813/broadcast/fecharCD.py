# Send UDP broadcast packets

MYPORT = 5000

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

data = 'eject -t' 
s.sendto(data, ('<broadcast>', MYPORT))
