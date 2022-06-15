# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

# -----UTILIZANDO FOR LOOP-----
# while True:
#     numero=int(input('Digite um número: '))
#     if numero < 0:
#         break
#     for tabuada in range(0,11,1):
#         print(f'{numero} x {tabuada} = {numero*tabuada}')
# print('Acabou!')

# --------------------------------------------------------------------

# ------UTILIZANDO WHILE LOOP------
# tabuada=-1
# while True:
#     numero=int(input('Digite um número (Número negativo para parar o programa): '))
#     if numero < 0:
#         break
#     while tabuada < 10:
#         tabuada+=1
#         print(f'{numero} x {tabuada} = {numero*tabuada}')
# print('Acabou!!!')