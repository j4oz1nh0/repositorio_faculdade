while True:
    try:
        notas, consultas = map(int, input().split())
        nota_vet = [0 for i in range(notas)]
        for i in range (notas):
            nota_vet[i] = int(input())
        nota_vet.sort(reverse=True)
        for i in range(consultas):
            cons = int(input())
            print(nota_vet[cons-1])
    except EOFError:
        break