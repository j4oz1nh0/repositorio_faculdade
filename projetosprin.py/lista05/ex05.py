vetor = [0 for i in range(5)]
for i in range(5):
    add = int(input())
    while add>10 or add<0:
        add = int(input())
    vetor[i]= add
for i in range(5):
    print(vetor[i])