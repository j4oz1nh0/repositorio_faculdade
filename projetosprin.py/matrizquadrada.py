A= int(input())
while A!=0:
    matrizwhile = [[2**(j+i) for j in range (A)]for i in range (A)]
    maior = matrizwhile[A-1][A-1]
    largura = len(str(maior))
    for i in range(A):
        for j in range(A):

                print(f" {matrizwhile[i][j]:>{largura}}", end="")
        print()
    print()
    A = int(input())