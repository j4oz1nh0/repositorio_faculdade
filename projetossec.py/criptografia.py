matriz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
finais = ['a', 'b', 'c']
frase = str(input())
frase_mat = []
indice = -1
for i in range(len(frase)):
    frase_mat.append(frase[i])
for j in range(len(frase)):
    for i in range(len(matriz)-3):
        if matriz[i]==frase[j]:
            indice = (i + 3) % 26
            frase_mat[j]=matriz[indice]
    for i in range(23, len(matriz)):
        if matriz[i]==frase[j]:
            indice = (i + 3) % 26
            frase_mat[j]=finais[indice]
for i in range(len(frase_mat)):
    print(frase_mat[i], end="")