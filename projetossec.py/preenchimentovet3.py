v = [0 for i in range(100)]
a = float(input())
for h in range(100):
    if h==0:
        v[h]=a
    else:
        a=a/2
        v[h]=a
    print(f"N[{h}] = {v[h]:.4f}")