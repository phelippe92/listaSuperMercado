
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
"""

import f
import os
import time

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

    print('╔══════════════════════════════════════════════════════════╗')
    print('║    >>>>>>>>>>>>    Lista De Compras    <<<<<<<<<<<<<<    ║')
    print('╚══════════════════════════════════════════════════════════╝')
    print('* COMIDA')
    f.viewListas(listGeralComida)
    # f.view(listComida)  #   mostra um valor por linha
    print('* BEBIDA')
    f.view(listGeralBebida)
    print('____________________________________________________________')

    if (len(listGeralComida) or len(listGeralBebida)) == 0:
        f.menu(11)   #   print menu
    else:
        f.menu(1)
        
    a = f.acao()
    
    if a == '1':  #   adicionar
        os.system('clear')
        f.menu('adicionar')
        a = f.acao()
        if a == '1':  #   comida
            print('qual comida')
            while True:
                os.system('clear')

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
                listComida.insert(0, nome)
                f.add(listComida, listGeralComida)
            else:
                listComida[:] = []

        elif a == '2':    #   bebida
            os.system('clear')
            
            print('qual bebida')
            while True:
                os.system('clear')

                os.system('clear')
                f.view(listBebida)
                bebida = f.bebida()

                if bebida == 'sair':
                    break

                f.add(bebida, listBebida)
                f.add(listBebida, listGeralBebida)

    # z = input()
    # if z != '':
    #     break
