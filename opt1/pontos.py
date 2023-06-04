x1 = int(input("Digite o primeiro número: "))
y1 = int(input("Digite o segundo número: "))
x2 = int(input("Digite o terceiro número: "))
y2 = int(input("Digite o quarto número: "))

def distancia(x1, y1, x2, y2):
    resultado = (((x1 - x2)**2 + (y1 - y2)**2)**(1/2))
    if resultado >= 10:
        print("longe")
    else:
        print("perto")

distancia(x1, y1, x2, y2)