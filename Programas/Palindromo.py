from time import sleep
print('''
    ---------BEM VINDO!---------
    Este é um detector de PALÍNDROMOS!
    ''')
sleep(1)
frases=str(input('Digite sua frase/palavra para a verificação: ')).strip().lower()
size=len(frases)
tamanho=''
for frase in range(size,0,-1):
    tamanho+=frases[frase-1]
print(f'Sua frase é * \033[32m{frases}\033[m * e invertida ela fica assim * \033[35m{tamanho}\033[m *')
    
if frases==tamanho:
    print('É palindromo ')
else:
    print('Não é palindromo ')