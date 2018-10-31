from cryptography.fernet import Fernet

def criarChave(destino):
    print ("Criando a chave")
    arquivo = open(destino, "w")
    arquivo.write(Fernet.generate_key().decode('utf-8'))
    arquivo.close()

def recuperarChave(arquivo):
    return open(arquivo, 'r').read().encode('utf-8')

def criarAquivoSenha(senha):
    print("Criando arquivo com a senha criptografada")
    cipher_suite = Fernet(recuperarChave("chave.txt"))
    arquivo = open("senha.txt", "w")
    arquivo.write(cipher_suite.encrypt(senha.encode('utf-8')).decode('utf-8'))
    arquivo.close()

def recuperaSenha(arquivo):
    cipher_suite = Fernet(recuperarChave("chave.txt"))
    return cipher_suite.decrypt(open(arquivo, 'r').read().encode('utf-8')).decode('utf-8')

#criarAquivoSenha("Uma Merda")
#criarChave("chave.txt")
#ocTDCPiIGwSpX_B0xOPL7fHvDhrGDRMeRsqj9Hrl620=
#print (recuperaSenha("senha.txt"))
