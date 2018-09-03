#!/usr/bin/python3

import socket
import os

HOST = '10.20.2.5'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
os.system('clear')
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST,PORT))
print('\nDigite suas mensagens')
print('Para sair use CTRL+X\n')
mensagem = input('Digite algo: ')

# Enviando a mensagem para o Servidor TCP através da conexão
while mensagem != '\x18':
    tcp.send(mensagem.encode('utf-8'))
    mensagem = input('Digite algo: ')
# Fechando o Socket
tcp.close()
