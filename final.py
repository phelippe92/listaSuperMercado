
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

    print('╔══════════════════════════════════════════════════════════╗')
    print('║    >>>>>>>>>>>>    Lista De Compras    <<<<<<<<<<<<<<    ║')
    print('╚══════════════════════════════════════════════════════════╝')
    print('* COMIDA')
    f.viewListas(listGeralComida)
    # print(listGeralComida)
    # f.view(listComida)  #   mostra um valor por linha
    print('* BEBIDA')
    f.viewListas(listGeralBebida)
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

                # listComida.insert(0, horario)
                # listComida.insert(0, nome)
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

                # listBebida.insert(0, horario)
                # listBebida.insert(0, nome)
                f.add(listBebida[:], listGeralBebida)

    # z = input()
    # if z != '':
    #     break
