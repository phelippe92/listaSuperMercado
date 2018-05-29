import os

def view(lista):    #   mostra um valor por linha
    for n in lista:
        print('     ', n)

def add(adicionado, destino):
    destino.append(adicionado)

def comida():  
    os.system('clear')    
    a = input('Digite sair p/ sair\nEnter p/ continuar\n')
    if a == 'sair':
            return 'sair'

    nome = input('Nome Do Alimento \n>> ')
    qt = input('Quantidade \n>> ')
    vegetariano = input('Vegetariano?\n1. sim\n2. nao\n>> ')
    
    if vegetariano == ('2' or 'nao'):
        vegetariano = False

    comida = (nome, int(qt), bool(vegetariano))
    
    return comida

def bebida():  
    os.system('clear')
    a = input('Digite sair p/ sair\nEnter p/ continuar\n')
    if a == 'sair':
            return 'sair'

    nome = input('Nome Da Bebida \n>> ')
    qt = input('Quantidade \n>> ')
    alcoolica = input('Alcoolica\n1. sim\n2. nao\n>> ')
    
    if alcoolica == ('2' or 'nao'):
        alcoolica = False

    bebida = (nome, int(qt), bool(alcoolica))

    return bebida

def acao():
    a = input('>> ')
    return(a)

#   PRINT
def menu(a): #   a = qual menu
    #   MENU INICIAL
    if a == 11:
        print('1. Adicionar')

    elif a == 1:
        print('1. Adicionar             2. Remover          3. Vizualizar')

    #---------------------x-------------------x------------------
    #   ADICIONAR
    elif a == 'adicionar':
        os.system('clear')  

        print('ADICIONAR')
        print('\n')
        print('1. Comida        2. Bebida')

    #---------------------x-------------------x------------------
    #   REMOVER
    elif a == 'remover':
        os.system('clear')  

        print('REMOVER')
        print('\n')
        