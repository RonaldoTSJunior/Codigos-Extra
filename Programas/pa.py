'''Progressão aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
FORMULA: 
-----Em programação Python, escrevemos assim:
ultimo = primeiro + (n-1)*r-----
'''
termo_inicial=int(input('Digite o primeiro elemento: '))
razao=int(input('Digite a razão: '))
n=int(input('Quantos elementos exibir: '))
ultimo=termo_inicial+(n-1)*razao
ultimo+=1
for pa in range(termo_inicial,ultimo,razao):
    print(pa,end=' → ')
print('Acabou!')