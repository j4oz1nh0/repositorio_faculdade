vetor = [int(input()) for i in range(20)]
maior = 0
menor = 0
marcador0 = 0
for i in range(20):
    if vetor[i]>maior:
        maior = vetor[i]
    if vetor[i]<menor or marcador0 == 0:
        menor= vetor[i]
        marcador0+=1
print(maior)
print(menor)