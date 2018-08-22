mensagem = "/m Ninho teste de envio"
print (mensagem)
comando = mensagem.split(" ")[0]
nick = mensagem.split(" ")[1]
remover = "{} {} ".format(comando, nick)
msg = mensagem.replace(remover, "")
print (msg)
