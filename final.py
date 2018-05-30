
#   LISTA SUPERMERCADO

"""   
    lista geral
        adicionar
            comida
                vegetariana(true)
                    salvar
            bebida
                alcoolica(true)
                    salvar
        remover
            lista geral
                sub-lista
                    comida
                    bebida

        vizualizar
            comida
                vegetariana
                        for n in listaComida:
                            if n[2] == True
                                print n
                != vegetariana
            bebida
"""

import f
import os
from datetime import datetime

listGeralComida = []
listGeralBebida = []
listComida = []
listBebida = []
# ╔═╦═╗
# ║ ║ ║
# ╠═╬═╣
# ╚═╩═╝
#  START
while True:
    os.system('clear')

    #   primeira tela
    f.menu('telaLista')
    print('* COMIDA')
    f.viewListas(listGeralComida)
    print('* BEBIDA')
    f.viewListas(listGeralBebida)
    
    if (len(listGeralComida) or len(listGeralBebida)) != 0:
        f.menu(1)   #   print menu
    else:
        f.menu(11)
    #---------------------x-------------------x------------------
        
    a = f.acao()
    
    if a == '1':  #   adicionar
        os.system('clear')
        f.menu('adicionar')
        a = f.acao()
        if a == '1':  #   comida
            print('qual comida')
            listComida[:] = []
            while True:
                os.system('clear')

                f.view(listComida)
                comida = f.comida()
                
                if comida == 'sair':
                    break
                f.add(comida, listComida)
            
            os.system('clear')
            x = input('Salvar?\n1. Sim\n2. Nao\n>> ')
            if x == ('1' or 'sim'):
                nome = input('Nome da lista:\n>> ')

                now = datetime.now()
                data = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
                time = str(now.hour)+':'+str(now.minute)+':'+str(int(now.second))
                horario = '['+data+' '+time+']'
                
                listComida[0:0] = [nome+' '+horario]

                f.add(listComida[:], listGeralComida)

        elif a == '2':    #   bebida
            print('qual bebida')
            listBebida[:] = []
            while True:
                os.system('clear')

                f.view(listBebida)
                bebida = f.bebida()

                if bebida == 'sair':
                    break

                f.add(bebida, listBebida)
                
            os.system('clear')
            x = input('Salvar?\n1. Sim\n2. Nao\n>> ')
            if x == '1' or x == 'sim' or x == 's':
                nome = input('Nome da lista:\n>> ')
                
                now = datetime.now()
                data = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
                time = str(now.hour)+':'+str(now.minute)+':'+str(int(now.second))
                horario = '['+data+' '+time+']'

                listBebida[0:0] = [nome+' '+horario]

                f.add(listBebida[:], listGeralBebida)

    elif a == '4':
        break


        l = ['nome+horario', comida('nome', qt, bool)]
