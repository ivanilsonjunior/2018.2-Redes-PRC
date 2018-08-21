# Retirado de https://docs.python.org/3/library/socket.html
# Echo server program
import socket

HOST = ''                 # Abre em todos os IPs da maquina
PORT = 2500              # Porta acima dos 1024 para garantir permissao
online = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(4)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Conectado por ', addr)
            while True:
                data = conn.recv(1024)
                dado = data.decode('utf-8')
                comando = dado.split(" ")[0]
                if comando == "/e":
                    print ("Entrada selecionada")
                    nick = dado.split(" ")[1]
                    online.append(nick)
                    mensagem = "Bem vindo {}".format(nick)
                    conn.sendall(mensagem.encode("utf-8"))                
                if comando == "/s":
                    print ("Saida selecionada")
                if comando == "/m":
                    print ("Mensagem selecionada")
                if comando == "/q":
                    print ("Quem online selecionada")
                    conn.sendall(str(online).encode("utf-8"))

                if not data: break
            #print ("comando: ", comando)
            #data += b" :)"
            #conn.sendall(data)
