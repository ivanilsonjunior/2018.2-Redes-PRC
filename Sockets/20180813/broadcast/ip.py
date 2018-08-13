# Send UDP broadcast packets

MYPORT = 5000

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

data = 'echo $(ip address show up|grep inet|grep -v inet6|grep -v 127.0.0|cut -d" " -f6|cut -d/ -f1)' 
s.sendto(data, ('<broadcast>', MYPORT))
