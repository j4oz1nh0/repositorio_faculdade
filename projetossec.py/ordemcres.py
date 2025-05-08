inteiros = [0 for cadanumero in range(5)]
i=0
for repeticao in range (5):
    num = int(input())
    inteiros[repeticao]= num
while i< len(inteiros)-1:
    proximapos = i+1
    if inteiros[i]<inteiros[proximapos]:
        i = i+1
    else:
        break
if i==4:
    print("ordem crescente")
else:
    print("presentation error 100%")
    