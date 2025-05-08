import math
A = int(input())
for i in range (A):
    N1, opd, D1, op, N2, opd2, D2 = input().split()
    N1, D1, N2, D2= int(N1), int(D1), int(N2), int(D2)
    if op == '+':
        cima= (N1 * D2 + N2 * D1)
        baixo= (D1 * D2)
    elif op == '-':
        cima= (N1 * D2 - N2 * D1)
        baixo= (D1 * D2)
    elif op == '*':
        cima= (N1 * N2)
        baixo= (D1 * D2)
    elif op == '/':
        cima= (N1 * D2)
        baixo= (N2 * D1)
    mdc = math.gcd(cima, baixo)
    ciman = cima//mdc
    baixon = baixo//mdc
    print(f"{cima}/{baixo} = {ciman}/{baixon}")