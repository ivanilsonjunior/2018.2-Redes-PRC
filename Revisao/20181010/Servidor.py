# Retirado de https://docs.python.org/3/library/socket.html
# Echo server program
import socket

HOST = ''                 # Abre em todos os IPs da maquina
PORT = 5000              # Porta acima dos 1024 para garantir permissao

def hora():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5004))
        data = s.recv(1024)
        return data

def disco():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5003))
        data = s.recv(1024)
        return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Conectado por ', addr)
        horas = hora()
        discos = disco()
        data = "Hora: {} Disco: {}".format(horas.decode('utf-8'), discos.decode('utf-8'))
        while True:
            conn.sendall(data.encode('utf-8'))
            conn.close()
