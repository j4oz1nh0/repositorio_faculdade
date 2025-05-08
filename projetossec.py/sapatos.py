a = int(input())
tam41D= 0
tam41E = 0
tam40D = 0
tam40E = 0
tam39D = 0
tam39E = 0

for i in range(a):
    tamanho = str(input())
    if tamanho[3]=='D':
        if tamanho[0]=='4':
            if tamanho[1]=='1':
               tam41D +=1
            if tamanho[1]=='0':
                tam40D +=1
        if tamanho[0]==3 and tamanho[1]==9:
            tam39D+=1
    if tamanho[3]=='E':
        if tamanho[0]=='4':
            if tamanho[1]=='1':
               tam41E +=1
            if tamanho[1]=='0':
                tam41E +=1
        if tamanho[0]==3 and tamanho[1]==9:
            tam39E+=1