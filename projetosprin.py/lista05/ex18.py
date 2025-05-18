import random
matriz = [[random.randint(1, 10) for j in range(15)]for i in range (15)]
maior = -1
for i in range(15):
    for j in range(15):
        if matriz[i][j]>maior:
            maior=matriz[i][j]
largura= len(str(maior))
for i in range(15):
    for j in range(15):
        if j == 14:
            print(f"{matriz[i][j]:>{largura}}")
        else:
            print(f" {matriz[i][j]:>{largura}}", end=" ")