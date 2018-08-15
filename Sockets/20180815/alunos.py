import os
import sys
# Receive UDP packets transmitted by a broadcasting service
arquivo="alunos.txt"
matriculas=[]
with open(arquivo) as a:
    for line in a:
        matriculas.append(line.strip().split(':')[1])

if sys.argv[1] == "fim":
    for matricula in matriculas:
        print ("{}{}".format(matricula[-2], matricula[-1]))
else:
    for matricula in matriculas:
        print (matricula)
