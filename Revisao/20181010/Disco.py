# Retirado de https://docs.python.org/3/library/socket.html
# Echo server program
import socket
import os
import pprint

HOST = ''                 # Abre em todos os IPs da maquina
PORT = 5003              # Porta acima dos 1024 para garantir permissao
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Conectado por ', addr)
        while True:
            disco = os.popen("df -h|grep sda1").readlines()
            data = str(pprint.saferepr(disco)).encode("utf-8")
            conn.sendall(data)
            conn.close()
