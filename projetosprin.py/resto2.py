A = int(input())
B=[]
for i in range (1, 10000):
    if i%A == 2:
        B.append(i)
N = 0
while N < len(B):
    print(B[N])
    N = N + 1