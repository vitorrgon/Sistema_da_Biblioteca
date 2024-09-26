from Sistema_da_Biblioteca.funções.interface import *
from Sistema_da_Biblioteca.funções.arquivo import *
from Sistema_da_Biblioteca.funções.interface import *
from Sistema_da_Biblioteca.funções.cores import *
from time import sleep

arqlivros = 'livros.txt'


if not verArq(arqlivros):
    criarArq(arqlivros)
while True:
    resp = menu(['Consultar Livros','Cadastrar Livros','Remover Livro','Emprestar Livro','Devolver Livro','Sair'])
    print(d["padrao"])
    sleep(1)
    if resp == 1:
        cabeçalho('Opção 1')
        lerArq(arqlivros)
    elif resp == 2:
        cabeçalho('Novo cadastro de Livros')
        idlivro = str(input('Digite o ID do livro: '))
        try:
            livnome = str(input('Digite o nome do livro: '))
        except:
            print('Por favor, tente inserir novamente o nome do livro, é OBRIGATÓRIO!')
        autnome = str(input('Digite o nome do autor do livro: '))
        catnome = str(input('Digite o nome da categoria do livro: '))
        cadLivro(arqlivros,idlivro,livnome,autnome,catnome)
    elif resp == 3:
        ...
    elif resp == 4:
        ...
    elif resp == 5:
        ...
    elif resp == 6:
        print('Ok. Saindo do Sistema...')
        break
cabeçalho('Programa Encerrado')