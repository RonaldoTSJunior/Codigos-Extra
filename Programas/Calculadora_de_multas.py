escolha='s'
while escolha=='s':
    velocidade=float(input('Insira a velocidade atual: '))
    limite=velocidade-80
    if velocidade>80:
        print(f'A velocidade atual é {velocidade}, e passou {limite} do limite de velocidade! Sua multa será de R${limite*7:.2f}')
    else:
        print('Sua velocidade está dentro dos limite!')
    escolha=input('Deseja continuar? ').lower()
x=input('Pressione qualquer tecla para fechar: ').lower()