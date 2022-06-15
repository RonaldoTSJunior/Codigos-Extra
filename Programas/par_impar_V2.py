from random import randint
contador=0
soma=0
while True:
    nome=str(input('Digite seu nome: ')).capitalize().strip()
    print('-='*20)
    numero=int(input(f'Olá {nome}! Digite um número: '))
    print('-='*20)
    escolha=str(input('Par ou Ímpar? [P/I]: ')).upper().strip()
    print('-='*20)
    computador=randint(0,10)
    soma=numero+computador
    if soma % 2 == 0:
        if escolha=='P':
            contador+=1
            print(f'{nome} jogou {numero}, e o computador jogou {computador}. Total foi {soma} é PAR.')
            print(f'{nome} ganhou! PARABÉNS.')
        elif escolha=='I':
            print(f'{nome} jogou {numero}, e o computador jogou {computador}. Total foi {soma} é PAR.')
            print(f'{nome} perdeu! Tente Novamente.')
            break
        print('-='*20) 
    elif soma % 2 !=0:
        if escolha=='I':
            contador+=1
            print(f'{nome} jogou {numero}, e o computador jogou {computador}. Total foi {soma} é ÍMPAR.')
            print(f'{nome} ganho! PARABÉNS.')
        elif escolha=='P':
            print(f'{nome} jogou {numero}, e o computador jogou {computador}. Total foi {soma} é ÍMPAR.')
            print(f'{nome} perdeu! Tente Novamente.')
            break
    print(f'O total de vitórias consecutivas foi de {contador}')
