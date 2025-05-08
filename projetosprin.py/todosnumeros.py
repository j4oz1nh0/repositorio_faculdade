A = []
B, C = map (int, input().split())
if C>0 and B>0:
    if B>C:
        for i in range (C, B+1):
            A.append(i)
        print(' '.join(map(str, A)), f"Sum={sum(A)}")
    if C>B:
        for i in range (B, C+1):
            A.append(i)
        print(' '.join(map(str, A)), f"Sum={sum(A)}")
while C>0 and B>0:
    A.clear()
    B, C= map (int, input().split())
    if C>0 and B>0:
        if B>C:
            for i in range (C, B+1):
                A.append(i)
            print(' '.join(map(str, A)), f"Sum={sum(A)}")
        if C>B:
            for i in range(B, C+1):
                A.append(i)
            print(' '.join(map(str, A)), f"Sum={sum(A)}")


