
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

listGeral = []
listComida = []
listBebida = []

#  START
while True:
    os.system('clear')

    print('++++++++++    Lista de compras    ++++++++++')
    print('* COMIDA')
    f.view(listComida)
    print('* BEBIDA')
    f.view(listBebida)
    print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

    if len(listGeral) == 0:
        f.menu(11)   #   print menu
    else:
        f.menu(1)
        
    a = f.acao()
    
    if a == '1':  #   adicionar
        f.menu('adicionar')
        a = f.acao()
        if a == '1':  #   comida
            print('qual comida')
            while True:
                os.system('clear')

                f.view(listComida)
                comida = f.comida()
                
                if comida == 'sair':
                    break

                f.add(comida, listComida)
                f.add(listComida, listGeral)
        elif a == '2':    #   bebida
            os.system('clear')
            
            print('qual bebida')
            while True:
                os.system('clear')

                f.view(listBebida)
                bebida = f.bebida()

                if bebida == 'sair':
                    break

                f.add(bebida, listBebida)
                f.add(listBebida, listGeral)

    # z = input()
    # if z != '':
    #     break

    
    


