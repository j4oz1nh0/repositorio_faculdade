import random
vetor = [[random.randint(1, 10) for i in range(25)]for i in range(5)]
soma=0
print(vetor)
for i in range (5):
    print(vetor[i][0])
for i in range (5):
    soma+= vetor[i][4]
print(soma)