a = int(input())
resposta=0
for i in range(a):
    b, c = map(int, input().split())
    resposta = (b//c)+(b%c)
    print(resposta)