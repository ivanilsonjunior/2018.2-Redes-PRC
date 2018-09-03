#!/usr/bin/python3
import socket
import _thread
import os
HOST = ''      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está

#-------------------------------------------------------------------------
# Função chamada quando uma nova thread for iniciada
def conectado(con, cliente):
    print('\nCliente conectado:', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print('O Cliente {0} disse: {1}'.format(cliente,msg.decode('utf-8')))
    print('\nFinalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()
#-------------------------------------------------------------------------
# Bloco principal
os.system('clear')
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print('\nServidor TCP-THREAD iniciado no IP', HOST, 'na porta', PORT)

while True:
    con, cliente = tcp.accept()
    print('\nNova thread iniciada para essa conexão')
    # Abrindo uma thread para a conexão
    _thread.start_new_thread(conectado, tuple([con, cliente]))
tcp.close()
