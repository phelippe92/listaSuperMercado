import os
from datetime import datetime

def viewListas(lista):  #   mostra listas dentro da geral
    for n in lista:
        x = lista.index(n) + 1
        print('  └──» ', x,'. ', n[0])    # 0 = nomeda lista, 1 = horario

def view(lista):    #   mostra um valor por linha
    for n in lista:
        x = lista.index(n) + 1
        print('  └──» ', x,'. ', n)    # 0 = nomeda lista, 1 = horario

def add(adicionado, destino):
    destino.insert(0, adicionado)

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
        print('________________________________________________________________________')
        print('1. Adicionar         4. Sair')

    elif a == 1:
        print('________________________________________________________________________')
        print('1. Adicionar             2. Remover          3. Vizualizar       4. Sair')

    #---------------------x-------------------x------------------
    #   ADICIONAR
    elif a == 'adicionar':
        print('╔══════════════════════════════════════════════════════════════════════╗')
        print('║    >>>>>>>>>>>>>>>>>>>>>    ADICIONAR    <<<<<<<<<<<<<<<<<<<<<<<<    ║')
        print('╚══════════════════════════════════════════════════════════════════════╝')
        print('________________________________________________________________________')
        print('1. Comida        2. Bebida')

    #---------------------x-------------------x------------------
    #   REMOVER
    elif a == 'remover':
        os.system('clear')  

        print('REMOVER')
        print('\n')
    
    #---------------------x-------------------x------------------
    elif a == 'telaLista':
        print('╔══════════════════════════════════════════════════════════════════════╗')
        print('║    >>>>>>>>>>>>>>>>>>    Lista De Compras    <<<<<<<<<<<<<<<<<<<<    ║')
        print('╚══════════════════════════════════════════════════════════════════════╝')

def addComida(listComida):
        view(listComida)
        c = comida()
        
        if c == 'sair':
            return False
        else:
            add(c, listComida)
            return True

def addBebida(listBebida):
        view(listBebida)
        c = bebida()
        
        if c == 'sair':
            return False
        else:
            add(c, listBebida)
            return True

def save(list, listGeral):
    print('________________________________________________________________________')
    print('Enter -> Salvar         Outro -> Sair Sem Salvar')
    x = input('>> ')
    if x == '':
        nome = input('Nome da lista:\n>> ')

        now = datetime.now()
        data = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
        time = str(now.hour)+':'+str(now.minute)+':'+str(int(now.second))
        horario = '['+data+' '+time+']'
        
        list[0:0] = [nome+' '+horario]

        add(list[:], listGeral)

def adicionar(a, listComida, listBebida):
    # menu('adicionar')
    # a = input('>> ')
    if a == '1':  #   comida
        listComida[:] = []

        while True:
            os.system('clear')
            if not addComida(listComida): #   sair da lista
                break
        
        return 'comida'
        # os.system('clear')
        # save(listComida, listGeralComida) #   salvar lista

    elif a == '2':    #   bebida
        listBebida[:] = []
        while True:
            os.system('clear')
            if not addBebida(listBebida): #   sair da lista
                break
        
        return bebida
            
        # os.system('clear')
        # save(listBebida, listGeralBebida) #   salvar lista


def start(listGeralComida, listGeralBebida):
    #   primeira tela
    menu('telaLista')
    print('* COMIDA')
    viewListas(listGeralComida)
    print('\n* BEBIDA')
    viewListas(listGeralBebida)
    
    if (len(listGeralComida) or len(listGeralBebida)) != 0:
        menu(1)   #   print menu
    else:
        menu(11) 
