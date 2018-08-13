# Send UDP broadcast packets

MYPORT = 5000

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

data = 'xset -led 2 led on' 
s.sendto(data, ('<broadcast>', MYPORT))
time.sleep(1)
data = 'xset -led 2 led off' 
s.sendto(data, ('<broadcast>', MYPORT))
time.sleep(2)
data = 'xset -led 16 led on' 
s.sendto(data, ('<broadcast>', MYPORT))
time.sleep(1)
data = 'xset -led 16 led off' 
s.sendto(data, ('<broadcast>', MYPORT))
