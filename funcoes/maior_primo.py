def maior_primo(n):
    for i in range(n, 1, -1):
        if numero_primo(i):
            return i


def numero_primo(n):
    if n < 2:
        return False

    raiz = int(n**0.5)
    for i in range(2, raiz + 1):
        if n % i == 0:
            return False

    return True
