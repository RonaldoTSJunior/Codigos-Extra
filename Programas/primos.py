'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
n=int(input('Digite um número: '))
contador=0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[33m',end=' ')
        contador+=1
    else:
        print('\033[31m',end=' ')
    print(f'{c}\033[m',end=' ')
print(f'\nSeu número {n} foi divisível {contador} vezes!')
if contador % c == 2:
    print('Seu número é primo')
else:
    print('Seu número não é primo')