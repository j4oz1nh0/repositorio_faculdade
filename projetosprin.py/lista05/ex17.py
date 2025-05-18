import random
vetor = [[random.randint(1,10) for j in range(10)]for i in range(10)]
print(vetor)
for i in range(10):
    temp = vetor[2][i]
    vetor[2][i]=vetor[i][8]
    vetor[i][8]=temp
print(vetor)