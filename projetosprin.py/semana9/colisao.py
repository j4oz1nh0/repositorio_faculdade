repeticao = int(input())
for i in range(repeticao):
    aj, ai, bj, bi, cj, ci, dj, di, rj, ri = [
    int(x) for x in input().strip().split(' ')]
    minj= min(aj, bj, cj, dj)
    maxj = max(aj, bj, cj, dj)
    mini = min(ai, bi, ci, di)
    maxi = max(ai, bi, ci, di)
    if minj<=rj<=maxj and mini<=ri<=maxi:
        print("1")
    else:
        print("0")
    '''
    N = int(input())

for _ in range(N):
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, Rx, Ry = [
        int(x) for x in input().strip().split(' ')]

    print(1 if Ax <= Rx <= Bx and Dx <= Rx <=
          Cx and Ay <= Ry <= Dy and By <= Ry <= Cy else 0)
'''