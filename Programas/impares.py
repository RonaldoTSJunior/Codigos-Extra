s=0
for num in range(1,501):
    if num % 2!=0:
        if num % 3==0:
            s+=num
print(f'A soma dos números impares multiplos de 3 é {s}!')