import math
divisor = 3
soma =1
for i in range(1,52):
    if i%2==1:
        soma = soma - (1/divisor)**3
        print(soma)
    elif i%2==0:
        soma = soma + (1/divisor)**3
    divisor = divisor + 2
pi = (soma*32)**(1/3)
print(pi)