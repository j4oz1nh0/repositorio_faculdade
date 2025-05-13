while True:
    try:
        a = int(input())
        if a % 2 != 0:
            a = a - 1
        lado_esq = []
        lado_dir = []
        pares = 0
        for i in range(a):
            tamanho, lado = input().split()
            tamanho = int(tamanho)
            if lado == 'D':
                lado_dir.append(tamanho)
            if lado == 'E':
                lado_esq.append(tamanho)
        for j in lado_esq:
            if j in lado_dir:
                pares += 1
                lado_dir.remove(j)
        print(pares)
    except EOFError:
        break