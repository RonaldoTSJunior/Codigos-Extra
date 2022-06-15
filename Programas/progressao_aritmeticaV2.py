# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('---------PROGRESSÃO ARITMÉTICA 2.0---------')
termo_inicial=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))
total=0
mais=10
contador=1
while mais !=0:
    total += mais
    print('Os 10 primeiros termos são:\n',end=' ')
    while contador <= total:
        print(f'{termo_inicial}',end=' → ')
        termo_inicial+=razao
        contador+=1
    print('PAUSA')
    mais=int(input('\nQuantos elementos deseja exibir mais? '))
print(f'\nFinalizando...')

