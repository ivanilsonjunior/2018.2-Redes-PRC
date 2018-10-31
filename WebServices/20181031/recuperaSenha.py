from cryptography.fernet import Fernet

chave = open('chave.txt', 'r').read() 
cipher_suite = Fernet(key)
cipher_text = open('senha.txt', 'r').read().encode('utf-8') 
senha = cipher_suite.decrypt(cipher_text)
