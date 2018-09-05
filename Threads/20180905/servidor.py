#!/usr/bin/python3
import socket
import _thread
import os
import time
import datetime
HOST = ''      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está

# Biblioteca que faz a conexao
import requests
# Biblioteca que le o HTML e faz a busca
from lxml import html
# O requests faz a conexao ao site usando http

import random

def noticiasGlobo():
    pagina = requests.get("http://www.globo.com")
    # Eh Gerado uma variavel de nome conteudo com o HTML da pagina
    conteudo = html.fromstring(pagina.content)
    # noticias eh o resultado da busca pela class hui-premium__title
    noticias = conteudo.xpath('//a[@class="topglobocom__content-title"]/text()')
    return noticias

#-------------------------------------------------------------------------
# Função chamada quando uma nova thread for iniciada
def conectado(con, cliente):
    print('\nCliente conectado:', cliente)
    while True:
       time.sleep(5)
       data = datetime.datetime.now()
       hora = data.strftime("%c")
       noticias = noticiasGlobo()
       noticia = noticias[random.randrange(len(noticias))]
       retorno =  "{} - {}".format(hora, noticia)
       con.sendall(retorno.encode("utf-8")) 
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
