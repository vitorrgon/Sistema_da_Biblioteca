import re
from Sistema_da_Biblioteca.funções.interface import *
from Sistema_da_Biblioteca.funções.cores import *

#Criar e acessar arquivo


def verArq(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro ao tentar criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArq(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('Livros Cadastrados')
        for linha in arq:
            dado = linha.split(',')
            dado[3] = dado[3].replace('\n','')#irá alterar o último dado da linha para ler os arquivos
            print(f'{dado[0]:<1} - {dado[1]:<20} - {dado[2]:<8} - {dado[3]:>10}')

    finally:
        arq.close()


#Cadastro dos livros


def cadLivro(arq, id, livro, autor='não informado', categoria='não informado'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao acessar o arquivo')
    else:
        try:
            a.write(f'{id},{livro},{autor},{categoria}\n')
        except:
            print('Erro ao gravar os dados')
        else:
            print(f'O registro de {livro} foi concluído!')

    finally:
        a.close()