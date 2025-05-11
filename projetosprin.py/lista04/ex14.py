a = int(input())
vetor_nome = ["" for i in range(a)]
vetor_dolar=[0.0 for i in range(a)]
vetor_quant=[0.0 for i in range(a)]
for i in range (a):
    vetor_nome[i]= str(input())
    vetor_dolar[i]= float(input())
    vetor_quant[i] = int(input())
    vetor_dolar[i]= vetor_dolar[i]*vetor_quant[i]
for i in range(a):
    print(vetor_nome[i])
    print(vetor_dolar[i], "dolar(es)")
    print("{:.2f}".format(vetor_dolar[i]*5.65), "real(is)")