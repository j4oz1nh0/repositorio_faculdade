A= int(input())
B= int (input())
C=[]
a = 0
b = 0
a = A
b = B
if A>B:
    A = A - 1
    while A>B :
        if A%2==1 or A%2==-1:
            C.append(A)
        A = A - 1
    print(sum(C))
if B>A:
    B=B - 1
    while B>A:
        if B%2==1 or B%2==-1:
            C.append(B)
        B=B-1
    print(sum(C))
if a == b:
    print(0)
