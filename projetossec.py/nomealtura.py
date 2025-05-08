n = ["" for h in range(2)]
a = [0.0 for b in range(2)]
alt = 0.0
pos= -1
for i in range (2):
    altura = float(input())
    nome = str(input())
    n[i] = nome
    a[i]= altura
    if altura>alt or alt==0:
        alt=altura
for alturas in range (len(a)): #mesma funcao do index
    if a[alturas]==alt:
        pos = alturas
print(a[pos], n[pos])




