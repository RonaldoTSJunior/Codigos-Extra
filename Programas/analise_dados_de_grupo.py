#  Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
maior_18=0
menos_20=0
homens=0
while True:
    nome=str(input('Digite seu primeiro nome: ')).capitalize().strip()
    sexo=str(input('Digite seu gênero [M/F]: ')).upper().strip()
    idade=int(input('Digite sua idade: '))
    escolha=str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if idade>18:
        maior_18+=1
    if sexo=='M':
        homens+=1
    if sexo=='F' and idade < 20:
        menos_20+=1
    if escolha=='N':
        print(f'Neste grupo temos {maior_18} maiores de 18.\nNeste grupo {homens} homens foram cadastrados.\nE neste grupo temos {menos_20} mulheres com menos de 20 anos!')
        break
print('Finalizando...')