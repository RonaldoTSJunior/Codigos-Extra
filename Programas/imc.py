# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
escolha='s'
while escolha=='s':
    print('''
    * CALCULADORA DE IMC *
    ''')
    peso=float(input('Seu peso:  '))
    altura=float(input('Sua altura:  '))
    imc=peso/(altura*altura)
    if imc<18.5:
        print(f'Você está abaixo do peso!\nSeu IMC é {imc:.2f}')
    elif imc>18.5 and imc<25:
        print(f'Parabéns! Você está no peso ideal.\nSeu IMC é {imc:.2f}')
    elif imc>25 and imc<30:
        print(f'Atenção, você está com sobrepeso!\nSeu IMC é {imc:.2f}')
    elif imc>30 and imc<40:
        print(f'Atenção, você atingiu a obesidade.\nSeu IMC é {imc:.2f}')
    else:
        print(f'Cuidado! Obesidade mórbida, procure um profissional.\nSeu IMC é {imc:.2f}')
    escolha=str(input('DESEJA REFAZER A OPERAÇÃO?\n[S/N]  '))