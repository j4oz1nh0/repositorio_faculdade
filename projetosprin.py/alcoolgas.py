A, G, Ra, Rg = map(float, input().split())
if (Ra/A)<(Rg/G):
    print("G")
elif (Ra/A)>(Rg/G):
    print("A")
else:
    print("G")