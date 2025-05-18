v = [0 for i in range (30)]
for i in range (30):
    v[i] = int(input())
for i in range (30):
    if i%2 ==0:
        v[i]=0
print(v)