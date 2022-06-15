'''Desenvolva um programa que leia 6 números inteiros,
e mostre a soma apenas daqueles q forem pares.
Se o valor digitado for impar, desconsidere'''
s=0
for n in range(1,7):
    n=int(input('Digite um número: '))
    if n % 2==0:
        s+=n
print(f'A soma dos números pares é {s}.')
