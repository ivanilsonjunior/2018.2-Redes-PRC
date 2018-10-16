import psycopg2
conexao = "dbname=aula user=postgres host=localhost"
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
conn = psycopg2.connect(conexao)
cur = conn.cursor()
cur.execute("insert into contatos (nome, telefone) values ( '{}', '{}')".format(nome, telefone))
conn.commit()
conn.close()

