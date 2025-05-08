A = float(input())
if A <= 400.00:
    por = A * 0.15
    print("Novo salario: {:.2f}".format(A+por))
    print("Reajuste ganho: {:.2f}".format(por))
    print("Em percentual: 15 %")
if A > 400.00 and A<= 800.00:
    por = A * 0.12
    print("Novo salario: {:.2f}".format(A + por))
    print("Reajuste ganho: {:.2f}".format(por))
    print("Em percentual: 12 %")
if A > 800.00 and A<=1200.00:
    por = A * 0.1
    print("Novo salario: {:.2f}".format(A+por))
    print("Reajuste ganho: {:.2f}".format(por))
    print("Em percentual: 10 %")
if A > 1200.00 and A<=2000.00:
    por = A * 0.07
    print("Novo salario: {:.2f}".format(A+por))
    print("Reajuste ganho: {:.2f}".format(por))
    print("Em percentual: 7 %")
if A > 2000.00:
    por = A * 0.04
    print("Novo salario: {:.2f}".format(A + por))
    print("Reajuste ganho: {:.2f}".format(por))
    print("Em percentual: 4 %")