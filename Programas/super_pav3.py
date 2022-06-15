# Crie uma progressao_aritmetica
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
elementos=1
while elementos != 0:
    termo_inicial=int(input('Digite o primeiro termo: '))
    razao=int(input('Digite a razao: '))
    elemento=int(input('Digite quantos elementos deseja exibir: '))
    print('Os elementos do termo é:\n',end=' ')
    if elemento != 0:
        print(f'{termo_inicial}',end=' → ')
        termo_inicial+=razao
        elementos=elementos-1
    elif elemento==0:
        print('Finalizando...')
print('Pronto! Finalizado.')