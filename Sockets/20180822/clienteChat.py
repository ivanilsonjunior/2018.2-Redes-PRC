# Retirado de https://docs.python.org/3/library/socket.html
# Echo client program
import socket

HOST = 'localhost'        # Servidor Remoto, pode ser usado o IP
PORT = 2522              # Porta do servidor que está esperando a conexão
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b'/q Yan')
#    data = s.recv(1024)
#print('Recebido: ', repr(data))

def menuCliente():
    print('Programa de chat:')
    print('1 - Entra no Chat')
    print('2 - Ver quem está no Chat')
    print('3 - Manda msg para o Chat')
    print('4 - Ver mensagens')
    print('5 - Sai no Chat')
    print('0 - Sai no Programa')
    return input("Digite uma opcao: ")

def entra(nick):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = "/e {}".format(nick)
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
        print('Recebido: ', repr(data))

def quem():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = "/q"
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
        print('Recebido: ', repr(data))

def msg(mensagem):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = "/m {}".format(mensagem)
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
        print('Recebido: ', repr(data))

def sai(nick):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = "/s {}".format(nick)
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
        print('Recebido: ', repr(data))

def ver():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = "/?".format(nick)
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
        print('Recebido: ', repr(data))

nick = ""

while True:
    opcao = menuCliente()
    if opcao == "0":
        break
    if opcao == "1":
        nick = input("Digite o nick: ")
        entra(nick)
    if opcao == "2":
        quem()
    if opcao == "3":
        mensagem = input("Digite a mensagem: ")
        msg("{} {}".format(nick,mensagem))
    if opcao == "4":
        ver()
    if opcao == "5":
        sai(nick)
        nick = ""






