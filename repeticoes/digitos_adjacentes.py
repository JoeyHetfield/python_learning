#  Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

n = input('Digite um número inteiro: ')
adjacente = False

for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        adjacente = True
        break
    
if adjacente:
    print('sim')
else:
    print('não')