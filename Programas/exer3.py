# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 
#------------------------------------------------------------------
# 1 para binário,
# 2 para octal  
# 3 para hexadecimal.
nova_conversao='s'
while nova_conversao=='s':   
    print('''---------REGRAS PARA A CONVERSÃO---------
    [1] Binário
    [2] Octal
    [3] Hexadecimal
    ''')
    numero=int(input('Digite um número inteiro: '))
    base=int(input('Escolha a sua base de conversão: '))
    if base==1:
        print('Você escolheu a conversão para BINÁRIO, aqui está sua resposta:',bin(base))
    elif base==2:
        print('Você escolheu a conversão para OCTAL, aqui está sua resposta:',oct(base))
    else:
        print('Você escolheu a conversão para HEXADECIMAL, aqui está sua resposta:',hex(base))
    nova_conversao=str(input('Deseja repetir o processo?\nS/N  ')).lower()