import time
import emoji
print('''
    CONTAGEM REGRESSIVA...
    ''')
for c in range(10,-1,-1):
    time.sleep(1)
    print(c)
print(emoji.emojize(':fireworks:'))
print('FIM!')