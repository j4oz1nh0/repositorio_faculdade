vetor = [int(input()) for i in range(15)]
maior = 0
maiorpos = -1
menor = 0
menorpos = -1
marcador0 = 0
for i in range(15):
    if vetor[i]>maior:
        maior = vetor[i]
        maiorpos = i
    if vetor[i]<menor or marcador0 == 0:
        menor= vetor[i]
        menorpos = i
        marcador0+=1
print(maiorpos)
print(menorpos)