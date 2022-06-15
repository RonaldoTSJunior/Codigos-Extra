print('---------CALCULO FATORIAL---------')
n=int(input('Digite um número '))
contador=1
fatorial=1
while contador <= n:
    fatorial*=contador
    contador+=1
    print(f'{n}!= {n}*{contador-1} = {fatorial}')
print('Acabou!')