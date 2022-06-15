# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# # Seu programa deverá realizar a operação solicitada em cada caso.
from secrets import choice
from time import sleep
print('''
      ---------MENU DE OPÇÕES---------
                 [REGRAS]
     * Digite dois números inteiros e escolha uma das opções abaixo ↓ *
           * [ 1 ] somar
           * [ 2 ] multiplicar
           * [ 3 ] maior
           * [ 4 ] novos números
           * [ 5 ] sair do programa
    ''')
sleep(1)
n1=int(input('* Digite um valor: '))
n2=int(input('* Digite outro valor: '))
opcao=0
while opcao!=5:
    opcao=int(input('* Escolha uma opção: '))
    if opcao==1:
        soma=n1+n2
        print(f'''
              * Opção escolhida foi [SOMAR] *
              .
              .
              .
              A soma de seus números é: {soma}''')
    elif opcao==2:
        multiplicar=n1*n2
        print(f'''
              * Opção escolhida foi [MULTIPLICAR] *
              .
              .
              .
              A multiplicação de seus números é: {multiplicar}''')
    elif opcao==3:
        if n1==n2:
            print(' * Os dois valores são iguais! *')
        elif n1 > n2:
            maior=n1
            print(f'''
                * Opção escolhida foi [MAIOR] *
                .
                .
                .
                O maior de seus números é {maior}
                ''')
        else:
            maior=n2
            print(f'''
                * Opção escolhida foi [MAIOR] *
                .
                .
                .
                O maior de seus números é {maior}
                ''')
    elif opcao==4:
        print(f'* Opção escolhida foi [NOVOS NÚMEROS] *')
        n1=int(input('* Digite um valor: '))
        n2=int(input('* Digite outro valor: '))
        opcao=int(input('* Escolha sua opção: '))
    elif opcao==5:
        print(f'''
              * Opção escolhida foi [SAIR DO PROGRAMA] *
                Finalizando...
              ''')
    else:
        print('✘ OPÇÃO INVÁLIDA. TENTE NOVAMENTE! ✘')
    print('=-='*10)
print('Programa finalizado.')