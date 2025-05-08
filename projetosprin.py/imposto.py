A= float(input())
if A<2000.00:
    print("Isento")
elif A> 2000.00 and A<=3000.00:
    A= A-2000.00
    B = A*0.08
    print("R$ {:.2f}".format(B))
elif A>3000.00 and A<=4500.00:
    A = A - 2000.00
    B = 1000.00
    C = A- B
    B = B*0.08
    C = C*0.18
    print("R$ {:.2f}".format(B+C))
elif A>4500.00:
    A = A - 2000.00
    B = 1000.00
    C = 1500.00
    D = A - B - C
    B = B * 0.08
    C = C * 0.18
    D = D * 0.28
    print("R$ {:.2f}".format(B+C+D))