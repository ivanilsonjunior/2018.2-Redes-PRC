import random
maxN = int(input("Escolha o maior numero para que eu possa escolher: "))
numero = random.randint(1,maxN)
acertou = False
tent = 0
while (not acertou):
	tent += 1
	digitado = int(input("Digite um número: "))
	if (numero == digitado):
		print("Acertou!!! em {} tentativas.".format(tent))
		acertou = True
	else:
		if (digitado > numero):
			print ("Tentativa {} - Errou, {} é maior".format(tent, digitado))
		else:
			print ("Tentativa {} - Errou, {} é menor".format(tent, digitado))

