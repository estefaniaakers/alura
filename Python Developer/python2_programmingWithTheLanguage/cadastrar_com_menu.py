# -*- coding: UTF-8 -*-
def listar(nomes):
    print ("Listando nomes: ")
    for nome in nomes:
        print (nome)

def cadastrar(nomes):
    print("Digite o nome: ")
    nome = input()
    nomes.append(nome)
    print (nomes)

def menu():
    nomes = []
    escolhe = ''
    while (escolhe != "0" ):
        print ("Digite 1 para cadastrar, 2 para listar e 0 para terminar")
        escolhe = input()
        if (escolhe == "1"):
            cadastrar(nomes)
        if (escolhe == "2"):
            listar(nomes)

menu()
