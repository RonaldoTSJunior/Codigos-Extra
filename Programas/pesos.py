# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
from time import sleep
print('''
      ---------BEM VINDO À BALANÇA!---------
      Por favor, aguarde um momento
      .
      .
      .
      ''')
sleep(1)
lista=[]
for pesos in range(5):
    nome=str(input('Digite seu primeiro nome: ')).capitalize()
    peso=float(input('Digite seu peso: '))
    print(f'''{nome} seu peso é {peso}''')
    lista+=[peso]                    #Para poder adicionar a var peso na lista, é necessário sinalizar com [] a var peso na soma.
print(f'O maior peso é',max(lista))      #Retorna o maior valor de uma lista
print(f'O menor peso é',min(lista))      #Retorna o menor valor de uma lista
