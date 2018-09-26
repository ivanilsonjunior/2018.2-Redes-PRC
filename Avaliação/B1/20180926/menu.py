def menu():
    print("Programa da Agenda:\n\t1 - Inserir\n\t2 - Apagar\n\t3 - Listar\n\t0 - sair")
    return input("Digite uma opção: ")

def inserir():
    print ("Aqui voce deve recuperar os dados da agenda e inserir no banco")


def apagar():
    print ("Aqui voce deve receber o contato que vc queira apagar e apagar no banco")

def listar():
    print ("Aqui voce deve listar todos os contatos no banco")

opcao = menu()
while (opcao != '0'):
    if opcao == '1':
        print ("1 - Inserir")
        inserir()
    if opcao == '2':
        print ("2 - Apagar")
        apagar()
    if opcao == '3':
        print ("3 - Listar")
        listar()
    opcao = menu()
    
