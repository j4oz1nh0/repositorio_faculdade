num_conta= [0]*100
agencia = [""]*100
saldo = [0.0]*100
agencias = []
saldo_agencias = []
saldopos=0
saldoneg=0
for i in range(100):
    num_conta[i] = int(input())
    agencia[i] = input()
    saldo[i] = int(input())
    if saldo[i]>0:
        saldopos+=1
    else:
        saldoneg+=1
    nova_agencia = True
    for j in range(len(agencias)):
        if agencia[i]==agencias[j]:
            saldo_agencias[j]+=saldo[i]
            nova_agencia=False
            break
    if nova_agencia:
        agencias.append(agencia[i])
        saldo_agencias.append(saldo[i])
for i in range(100):
    print(agencia[i])
    print(saldo[i])
    if saldo[i]>=0:
        print("e positivo")
    if saldo[i]<0:
        print("e negativo")
for i in range(len(agencias)):
    print(agencias[i])
    print(saldo_agencias[i])
saldoper = (saldoneg/(saldopos+saldoneg))*100
print("{:.2f}%".format(saldoper))

