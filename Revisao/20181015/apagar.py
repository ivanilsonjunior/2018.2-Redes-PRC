import psycopg2


conexao = "dbname=aula user=postgres host=localhost"
conn = psycopg2.connect(conexao)
cur = conn.cursor()
cur.execute("select * from contatos")
resultado = cur.fetchall()
for contato in resultado:
    print ("Id: {} Nome: {} Telefone: {}".format(contato[2], contato[0], contato[1]))


idContato = input("Digite o ID do contato a apgar: ")
conn = psycopg2.connect(conexao)
cur = conn.cursor()
cur.execute("delete from contatos where id={}".format(int(idContato)))
conn.commit()
conn.close()

