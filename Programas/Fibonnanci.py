# Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
print('---------Sequência de Fibonacci---------')
n=int(input('Digite um número: '))
ultimo=0
penultimo=1
print(f'A sequência de Fibonacci de {n} é:',end=' ')
while ultimo < n:
    print(ultimo,end=' ')
    ultimo,penultimo=penultimo, ultimo+penultimo
print('\nAcabou!')