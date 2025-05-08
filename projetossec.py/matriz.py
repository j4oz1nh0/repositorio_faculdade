matriz = [[j + i*2 for j in range (1, 3)] for i in range (2)]
matriz2 = [[j2 + i2*2 for j2 in range (1, 3)] for i2 in range (2)]
soma = [[0, 0],[0,0]]
for itotal in range (2):
    for jtotal in range (2):
        soma[itotal][jtotal]=matriz[itotal][jtotal]+matriz2[itotal][jtotal]
print(matriz)
print(matriz2)
for iprinto in range (2):
    for jprinto in range(2):
        if jprinto == 1:
            print(soma[iprinto][jprinto])
        else:
            print(soma[iprinto][jprinto], end=" ")