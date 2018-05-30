""" 
l = ['a', 'b', 'c']

a = open('test.txt', 'w')#

for n in l:
    a.write(n+' ')

a.close() 

a = open("test.txt")
v = []
v.append(a.readlines())
print(a.readlines())

a.close()

print('v = ', type(v), v) 
"""



""" 
import csv
lista = [] # você só precisa de uma lista - ela é uma matriz multidimensional

with open('meu.csv', newline='') as csvfile:
    # o nome 'spamreader' abaixo é só exemplo, poderia ser qq. coisa
    spamreader = csv.reader(csvfile, delimiter=',') # separe por vírgula

    # o módulo csv detectará novas linhas automaticamente
    for linha in spamreader:
        lista.append(linha)

# os elementos começam ser contados em zero, i.e. lista[0][1] == 'julian'
print(lista) # imprime a linha 2 da lista, inteira
# print(lista) # imprime apenas o segundo item da linha 2 
# """

f = open("meu.csv",'r')
texto = f.readlines()

x = 0

while x < len(texto):
    if texto[x] == "\n":
        local = texto.index(texto[x])
        texto.pop(local)
    else:
        texto[x] = texto[x].split(',')
        x += 1

# Esse for abaixo aqui é só para tirar o "\n" em algumas strings, é opcional.

for i in texto:
    local = texto.index(i) # Local do i em texto
    for b in i:
        local2 = texto[local].index(b) # Local2 do b em i ( local )
        if "\n" in b:
            texto[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"


lista1, lista2 = texto
print("lista1 =",lista1)
print("lista2 =",lista2)
