escolhas='s'
while escolhas=='s':
    c=str(input('Deseja adicionar um nome? s/n ')).lower()
    if c=='n':
        print('Claudio é arquiteto! ')
    else:
        nome=str(input('Digite um nome: ')).capitalize()
        print(f'{nome} é arquiteto')
    escolhas=str(input('Deseja repetir o questionamento? s/n ')).lower()
x=input('Pressione qualquer tecla para fechar... ')