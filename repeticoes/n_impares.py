n = int(input('Digite um número: '))

base = 0
number = 0

while base < n:
    if number % 2 != 0:
        print(number)
        base += 1
    number += 1
