vetor = [i for i in range(50)]
for i in range(len(vetor)//2):
        temp = vetor[i]
        vetor[i]=vetor[len(vetor)-1-i]
        vetor[len(vetor)-1-i]=temp
for i in range(50):
    print(vetor[i])