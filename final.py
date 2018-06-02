
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
    f.start(listGeralComida, listGeralBebida)
   
    #---------------------x-------------------x------------------
        
    a = input('>> ')
    
    if a == '1':  #   adicionar
        os.system('clear')
        f.menu('adicionar')
        a = input('>> ')
        if a == '1':  #   comida
            listComida[:] = []

            while True:
                os.system('clear')
                if not f.addComida(listComida): #   sair da lista
                    break
            
            os.system('clear')
            f.save(listComida, listGeralComida) #   salvar lista

        elif a == '2':    #   bebidaa
            listBebida[:] = []
            while True:
                os.system('clear')
                if not f.addBebida(listBebida): #   sair da lista
                    break
                
            os.system('clear')
            f.save(listBebida, listGeralBebida) #   salvar lista

    elif a == '4':
        break

