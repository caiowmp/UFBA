pistas,pessoasPistas,alunos = map(int,input().split())

if(pistas * pessoasPistas >= alunos + 1):
    print("S")
else:
    print("N")