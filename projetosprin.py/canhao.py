import math
A, L, P, R = map(int, input().split())
F = A**2 + L**2 + P**2
D = math.sqrt(F)
if D <= 2*R:
    print("S")
else:
    print("N")