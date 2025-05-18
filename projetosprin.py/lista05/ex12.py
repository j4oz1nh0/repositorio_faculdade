produtos = ["" for i in range(15)]
valores = [0 for i in range(15)]
indicecaro = -1
indicebar = -1
valorbar= 0
valorcaro = 0
for i in range(15):
    nome = input()
    valor=int(input())
    produtos[i]=nome
    valores[i]=valor
    if valor>valorcar:
        valorcar= valor
        indicecaro =i
    if valor<valorbar or indicebar==-1:
        valorbar=valor
        indicebar = i
print(produtos[indicecaro])
print(produtos[indicebar])
produtoaleatorio = input("insira o nome de um produto")
indice=-1
for i in range(15):
    if produtoaleatorio==produtos[i]:
        indice=i
        break
if indice!=-1:
    print(valores[indice])
else:
    print("produto nao encontrado")

