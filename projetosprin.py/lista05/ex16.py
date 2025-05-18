matriz = [[0 for j in range(5)]for i in range((10))]
vetor =[0for i in range(10)]
soma = 0
for i in range(10):
    for j in range (5):
        matriz[i][j]=int(input())
        soma+= matriz[i][j]
    vetor[i]=soma
    soma=0
maior=0
indice=-1
for i in range(10):
    if vetor[i]>maior:
        maior=vetor[i]
        indice = i
print(maior)
print(indice)