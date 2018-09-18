import psycopg2


conexao = "dbname=aula user=postgres host=localhost"
conn = psycopg2.connect(conexao)
cur = conn.cursor()
cur.execute("select * from contatos")
resultado = cur.fetchall()
for contato in resultado:
    print (contato)
