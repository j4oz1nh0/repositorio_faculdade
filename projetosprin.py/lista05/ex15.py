import random
vetor = [[random.randint(1,10) for j in range(10)]for i in range(10)]
print(vetor)
for i in range(10):
    for j in range(10):
        if i!=j:
            print(vetor[i][j])
for i in range(10):
    for j in range(10):
        if i==j:
            print(vetor[i][j])
soma=0
for i in range(10):
    for j in range(10):
        soma+=vetor[i][j]
    print(soma)
produto=1
for j in range(10):
    for i in range(10):
        produto=vetor[i][j]*produto
    print(produto)