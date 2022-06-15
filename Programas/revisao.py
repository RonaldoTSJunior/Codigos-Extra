import random
import time
novamente='s'
while novamente=='s':
    print('''
    ---------BEM-VINDO---------
    VAMOS REVISAR ALGUNS EXERCICIOS DO GUANABARA?
    ''')
    exercicio=random.randint(1,51)
    time.sleep(1)
    print('Escolhendo... Por favor, aguarde! ')
    time.sleep(1)
    print('3')
    time.sleep(3)
    print('2')
    time.sleep(2)
    print('1')
    time.sleep(1)
    print(f'Pronto! O exercicio que deve revisar é: {exercicio}')
    novamente=str(input('Deseja escolher novamente?\nS/N  ')).lower()
    
