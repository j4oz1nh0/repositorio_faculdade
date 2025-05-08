
soma = 0
total = 0
while True:
    try:
        nome = input()
        distancia = float(input())
        soma = soma + 1
        total = total + distancia
    except EOFError:
        break
aa = total/soma
print("{:.1f}".format(aa))

