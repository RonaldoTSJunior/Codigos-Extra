# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from time import sleep
print('''
      ---------ANALISADOR COMPLETO---------
      Por favor, aguarde um instante!
      .
      .
      .
                 [INSTRUÇÕES]
      * Genêros = M para Masculino, F para feminino *          
      ''')
sleep(1)
contador_mulher=0
nome_homem_velho=''
soma_media=0
maior=0
for analisador in range(4):  
      nome=str(input('Digite o primeiro nome: ')).capitalize().strip()
      idade=int(input('Digite sua idade: '))
      sexo=str(input('Digite seu genêro: ')).upper().strip()
      soma_media+=idade
      media=soma_media/4
      if sexo=='M' and idade > maior:
            maior=idade
            nome_homem_velho=nome
      elif sexo=='F' and idade < 20:
            contador_mulher+=1
print(f'''
      A média de idade deste grupo é {media}
      O nome do homem mais velho é {nome_homem_velho}
      Neste grupo temos {contador_mulher} mulheres abaixo de 20 anos.
      ''')

      

    