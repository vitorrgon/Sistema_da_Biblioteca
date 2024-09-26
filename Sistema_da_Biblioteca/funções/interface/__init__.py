from Sistema_da_Biblioteca.funções.cores import *


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número\033[97m')
            return 0
        else:
            return n


def linha(tam=54):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print((d["pix"]),txt.center(54),(d["padrao"]))
    print(linha())


def menu(lista):

    cabeçalho('MENU PRINCIPAL da Biblioteca')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())

    opc = leiaInt('Sua Opção: ')
    return opc