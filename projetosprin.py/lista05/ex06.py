import random
vetor = [random.randint(1, 10) for i in range(100)]
marcador = 0
N = int(input())
for i in range(100):
    if vetor[i]== N:
        print("existe")
        marcador+=1
        break
if marcador==0:
    print("nao existe")