n = int(input('Digite um número para calcular seu fatorial: '))

if n == 0:
    print('O fatorial de 0 é 1')
else:
    fatorial = 1
    for i in range(n, 1, -1):
        fatorial *= i
    print(f'O fatorial de {n} é {fatorial}')