A1, B1, C1 = map(float, input().split())
A2, B2, C2 = map(float, input().split())
A1 = int(A1)
A2 = int(A2)
B1 = int(B1)
B2 = int(B2)
preco = B1*C1 + B2*C2
print("VALOR A PAGAR: R$ {:.2f}".format(preco))