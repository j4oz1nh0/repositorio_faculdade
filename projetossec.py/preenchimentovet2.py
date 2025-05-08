N = [0 for i in range(1000)]
T = int(input())
j =0
for h in range(1000):
    N[h]=j
    print(f"N[{h}] = {N[h]}")
    j+=1
    if j==T:
        j=0

