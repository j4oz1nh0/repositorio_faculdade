matriz = [[int(input()) for j in range(3)]for i in range(3)]
matriz2 = [[int(input()) for j in range(3)]for i in range(3)]
soma = [[0 for j in range(3)]for i in range(3)]
for i in range(3):
    for j in range(3):
        soma[i][j]=matriz[i][j]+matriz2[i][j]
for iprinto in range(3):
    for jprinto in range(3):
        if jprinto == 2:
            print(soma[iprinto][jprinto])
        else:
            print(soma[iprinto][jprinto], end=" ")