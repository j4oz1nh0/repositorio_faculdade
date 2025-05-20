vetor = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = int(input())
for i in range(a):
    frase = input()
    frase_mat = ["" for l in range(len(frase))]
    salto = int(input())
    for i in range(len(frase)):
        if frase[i] in vetor:
            indice = (vetor.index(frase[i]) - salto) % 26
            frase_mat[i]=vetor[indice]
    for h in range(len(frase_mat)):
        if h == len(frase_mat)-1:
            print(frase_mat[h])
        else:
            print(frase_mat[h], end="")
