#!/usr/bin/env python3 
import cgi
import psycopg2
#Conexao com o banco de dados
conexao = "dbname=aula user=postgres host=localhost password=aluno"
conn = psycopg2.connect(conexao)
#Recuperando valores do formulario
form = cgi.FieldStorage()
nome = form.getvalue("nome")
telefone = form.getvalue("telefone")
operacao = form.getvalue("operacao")
print ("Content-type: text/html\n\n" )
print ("<html><body>")
print ("<h1>{}</h1>".format(operacao))

def consultar():
    cur = conn.cursor()
    cur.execute("select * from contatos")
    resultado = cur.fetchall()
    for contato in resultado:
        print ("<br/>Id: {} Nome: {} Telefone: {}".format(contato[0], contato[1], contato[2]))

def inserir():
    cur = conn.cursor()
    cur.execute("insert into contatos (nome, telefone) values ( '{}', '{}')".format(nome, telefone))
    conn.commit()
    print ("<br/>Contato {} e telefone {} Inserido".format(nome, telefone))
    conn.close()

def remover(idContato):
    cur = conn.cursor()
    cur.execute("delete from contatos where id={}".format(int(idContato)))
    conn.commit()
    conn.close()

if (operacao == "listar"):
    consultar()

if (operacao == "inserir"):
    inserir()

if (operacao == "remover"):
    idContato = form.getvalue("selecao")
    if idContato == None:
        cur = conn.cursor()
        cur.execute("select * from contatos")
        resultado = cur.fetchall()
        print ("<form action=\"agenda.py\" method=\"GET\">")
        print ("<input type=\"hidden\" id=\"remover\" name=\"operacao\" value=\"remover\">")
        for contato in resultado:
            print ("<br/><input type=\"radio\" name=\"selecao\" value=\"{}\">Nome: {} Telefone: {}".format(contato[0], contato[1], contato[2]))
        print ("</br><button type=\"submit\">Apagar</button>")
        print ("</form>")
    else:
        remover(idContato)
        print("</br> Contato removido")
  


#print ("<br>O nome foi: {}".format(nome))
#print ("<br>O telefone eh: {}".format(telefone))
print ("<br/><a href=\"javascript:history.back()\">Voltar</a>")
print ("</body></html>")
