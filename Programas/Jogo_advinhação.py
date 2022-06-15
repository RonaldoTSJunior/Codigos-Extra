# onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.
import random
from time import sleep
print('''
      ---------JOGO DE ADVINHAÇÃO---------
                    [REGRAS]
    Digite números de 1 a 10 para advinhar qual o número escolhido do computador
    
    Por favor, aguarde um momento!
    .
    .
    .
    ''')
sleep(1)
jogador=-1
contador=0
computador=random.randint(0,10)
print('''
    Ok! Já fiz minha escolha, agora é sua vez!
    Consegue advinhar o número que pensei?
    ''')
while jogador != computador:
    jogador=int(input('Digite um número: '))
    if jogador==computador:
        contador+=1
        print(f'Parabéns, você advinhou em \033[32m{contador}\033[m tentativas!\nO número escolhido foi \033[35m{computador}\033[m')
    else:
        contador+=1
        if jogador > computador:
            print('\033[34mMenos...\033[m')
        elif jogador < computador:
            print('\033[36mMais...\033[m')
print('Finalizando...')