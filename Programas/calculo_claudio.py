# CALCULO DO ARQUITETO CLAUDIO PARA PARTE DO CALCULO DE UMA VIGA.
#formula: x=0,68.29±√(0,68.d)²-4.0,272.(Md/bw.fcd)
#           ----------------------------------
#                         0,544
import math
opcao='s'
while opcao == 's':
    md=float(input('Digite o valor de MD: '))
    d=float(input('Digite o valor de D:  '))
    fcd=float(input('Digite o valor de FCD: '))
    bw=float(input('Digite o valor de BW: '))
    numero=0.68*d
    power1=math.pow(0.68,2)
    power2=math.pow(d,2)
    potencia=power1*power2
    parenteses=md/(bw*fcd)
    multiplicacao=(4*0.272)*parenteses
    subtracao=potencia-multiplicacao
    sqrt=math.sqrt(subtracao)
    x1=(sqrt+numero)/0.544
    x2=(numero-sqrt)/0.544
    print(f'''
          x¹ = {x1:.2f}
          x² = {x2:.2f}
          ''')
    opcao=str(input('Deseja refazer o processo? [S/N]  ')).lower()
print('Acabou!')
