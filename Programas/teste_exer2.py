e='s'
while e=='s':
    c=input('s/n: ')
    if c=='n':
        print('Dentro do if')
    else:
        n=input('nome: ')
        print(n)
    e=input('continua?')
print('Saiu do while')