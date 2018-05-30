from datetime import datetime


def viewListas(lista):
    now = datetime.now()
    data = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    time = str(now.hour)+':'+str(now.minute)+':'+str(int(now.second))
    # data = '[' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ']'+
    
    for n in lista:
        x = lista.index(n) + 1
        print('  └──» ', x,'. ', n[0], '[', data, time, ']')

def view(lista):    #   mostra um valor por linha
    for n in lista:
        x = lista.index(n) + 1
        print('  └──» ', x,'. ', lista[lista.index(n)])

def add(adicionado, destino):
    destino.append(adicionado)

def comida():      
    a = input('Digite sair p/ sair\nEnter p/ continuar\n>> ')
    if a == 'sair':
            return a

    nome = input('Nome Do Alimento \n>> ')
    qt = input('Quantidade \n>> ')
    vegetariano = input('Vegetariano?\n1. sim\n2. nao\n>> ')
    
    if vegetariano == ('2' or 'nao'):
        vegetariano = False

    if nome == '' or qt == '' or vegetariano == '':
        return None
    
    comida = (nome, int(qt), bool(vegetariano))
    
    return comida

def bebida():
    a = input('Digite sair p/ sair\nEnter p/ continuar\n')
    if a == 'sair':
            return 'sair'

    nome = input('Nome Da Bebida \n>> ')
    qt = input('Quantidade \n>> ')
    alcoolica = input('Alcoolica\n1. sim\n2. nao\n>> ')
    
    if alcoolica == ('2' or 'nao'):
        alcoolica = False
    if nome == '' or qt == '' or alcoolica == '':
        return None

    bebida = (nome, int(qt), bool(alcoolica))

    return bebida

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
        print('ADICIONAR')
        print('\n')
        print('1. Comida        2. Bebida')

    #---------------------x-------------------x------------------
    #   REMOVER
    elif a == 'remover':
        os.system('clear')  

        print('REMOVER')
        print('\n')

def acao():
    a = input('>> ')
    return(a)

