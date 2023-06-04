n = int(input('Digite um número para verificar se ele é primo: '))

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(f'{n} não é primo')
        break
else:
    print(f'{n} é primo')