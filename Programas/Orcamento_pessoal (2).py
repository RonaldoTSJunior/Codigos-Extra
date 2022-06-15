escolha = 's'

# INICIA A VARIAVEL DO SALDO COM O VALOR 0 PRA PODER USAR DENTRO DOS IF,ELIF,ELSE
saldo_final = 0
soma_despesas = 0   # INICIA A VARIAVEL SOMA_DESPESAS
soma_receitas = 0   # INICIA A VARIAVEL SOMA_RECEITAS
nome_receita = ''   # INICIA A VARIAVEL DA RECEITA
nome_despesa = ''  # INICIA A VARIAVEL DAS DESPESAS PRA IR ACRECENTANDO OS NOMES
nome_receita_input = ''
nome_despesa_input = ''

# DA UMA ESTUDADA EM 'O QUE SÃO VARIAVEIS LOCAIS E GLOBAIS PRA ENTENDER PRQ EU FIZ ISSO AQUI EM CIMA'

while escolha == 's':
    print('''--------ORCAMENTO PECOAL---------
    [1] INSERIR SALDO
    [2] INSERIR VALOR RECEITA
    [3] INSERIR VALOR DESPESA
    ''')

    choice = int(input('\nEscolha sua opção: '))

    if choice == 1:
        saldo = float(input('Digite o valor de seu saldo: '))
        # O += É A MESMA COISA Q SE FIZESSE ASSIM Ó (saldo_final = saldo_final + saldo)
        saldo_final += saldo

    elif choice == 2:
        nome_receita_input = str(input('Nome da receita: ')).capitalize()
        receita = float(input('Digite o valor de sua receita: '))
        saldo_final += receita
        soma_receitas += receita
        nome_receita += f' * {nome_receita_input} - {receita}\n'

    elif choice == 3:
        nome_despesa_input = str(input('Nome da despesa: ')).capitalize()
        despesa = float(input('Digite o valor de sua despesa: '))
        # O -= É A MESMA COISA Q SE FIZESSE ASSIM Ó (saldo_final = saldo_final - despesa)
        saldo_final -= despesa
        soma_despesas += despesa
        nome_despesa += f' * {nome_despesa_input} - {despesa}\n'

    else:
        print('\n!!! VALOR INVALIDO, TENTE NOVAMENTE !!!\n')

    print(f'Despesas:{soma_despesas}\n{nome_despesa} \nReceitas: {soma_receitas}\n{nome_receita} \nSeu saldo atual é de {saldo_final} ')
    escolha = str(input('Deseja repetir o processo? [S/N] ')).lower()
