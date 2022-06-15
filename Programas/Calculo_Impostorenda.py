# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00
import sys
escolha='s'
while escolha=='s':
    print('''
    BEM VINDO A RECEITA FEDERAL
    PARA O CALCULO DE SUA FOLHA DE PAGAMENTO, INSIRA OS DADOS ABAIXO
    .
    .
    .
    ''')
    hora_trabalhada=int(input('Digite o total de horas trabalhadas no mês:  '))
    vlr_horas=float(input('Digite o valor de seu hora trabalhada:  '))
    salario_bruto = hora_trabalhada*vlr_horas
    if salario_bruto<=900:
        print(f'Salário Bruto:         : R${(salario_bruto):.2f}\n(-) IR (ISENTO)        : R$ ISENTO\n(-) INSS (10%)         : R${(salario_bruto*0.10):.2f}\n    FGTS (11%)         : R${(salario_bruto*0.11):.2f}\n    TOTAL DESCONTOS    : R${(salario_bruto*0.10)}\n    Salário Liquido    : R${salario_bruto-(salario_bruto*0.10):.2f}')
    elif salario_bruto>900 and salario_bruto<=1500:
        print(f'Salário Bruto:         : R${(salario_bruto):.2f}\n(-) IR (5%)            : R${(salario_bruto*0.05):.2f}\n(-) INSS (10%)         : R${(salario_bruto*0.10):.2f}\n    FGTS (11%)         : R${(salario_bruto*0.11):.2f}\n    TOTAL DESCONTOS    : R${(salario_bruto*0.10)+(salario_bruto*0.05):.2f}\n    Salário Liquido    : R${salario_bruto-((salario_bruto*0.10)+(salario_bruto*0.05)):.2f}')
    elif salario_bruto>1500 and salario_bruto<=2500:
        print(f'Salário Bruto:         : R${(salario_bruto):.2f}\n(-) IR (10%)           : R${(salario_bruto*0.1):.2f}\n(-) INSS (10%)         : R${(salario_bruto*0.10):.2f}\n    FGTS (11%)         : R${(salario_bruto*0.11):.2f}\n    TOTAL DESCONTOS    : R${(salario_bruto*0.10)+(salario_bruto*0.1):.2f}\n    Salário Liquido    : R${salario_bruto-((salario_bruto*0.10)+(salario_bruto*0.1)):.2f}')
    else:
        print(f'Salário Bruto:         : R${(salario_bruto):.2f}\n(-) IR (20%))          : R${(salario_bruto*0.2):.2f}\n(-) INSS (10%)         : R${(salario_bruto*0.10):.2f}\n    FGTS (11%)         : R${(salario_bruto*0.11):.2f}\n    TOTAL DESCONTOS    : R${(salario_bruto*0.10)+(salario_bruto*0.2):.2f}\n    Salário Liquido    : R${salario_bruto-((salario_bruto*0.10)+(salario_bruto*0.2)):.2f}')
    escolha=str(input('Deseja refazer o cálculo?\n[S/N]  ')).lower()