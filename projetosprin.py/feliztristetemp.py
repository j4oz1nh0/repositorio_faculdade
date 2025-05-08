A, B, C = map(int, input().split())
if A>B and C>=B:
    print(":)")
elif B>A and B>=C:
    print(":(")
elif A<B<C:
    if C-B < B-A:
        print(":(")
    else:
        print(":)")
elif A>B>C:
    if B-C < A-B:
        print(":)")
    else:
        print(":(")
elif A==B:
    if C>B:
        print(":)")
    else:
        print(":(")