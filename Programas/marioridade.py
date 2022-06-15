# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from time import sleep
print('''
      ---------DETECTOR DE MAIORIDADE---------
      ''')
sleep(1)
contador_maior=0
contador_menor=0
for nascimento in range(0,7,1):
    nome=str(input('Digite seu primeiro nome: ')).capitalize()
    ano=int(input('Digite o seu ano de nascimento: '))
    idade=2022-ano
    maior_idade=18
    if idade >= maior_idade:
        contador_maior+=1
        print(f'''
              {nome} possui \033[35m{idade}\033[m.
              Parabéns! 
              Você atingiu a maior idade!
              ''')
    elif idade <= maior_idade:
        contador_menor+=1
        print(f'''
              {nome} possui \033[35m{idade}\033[m
              Ainda é menor de idade!
              Faltam {maior_idade-idade} anos!
              ''')
print(f'''
      {contador_maior} pessoas já atingiram ou passaram a maior idade.
      {contador_menor} pessoas ainda não atingiram a menor idade.
      ''')