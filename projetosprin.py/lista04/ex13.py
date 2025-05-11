total_carga = int(input())
peso = [0.0 for i in range (total_carga)]
preco = [0.0 for i in range (total_carga)]
somaprec = 0
somapes = 0
for i in range (total_carga):
    peso[i]= float(input())
    preco[i] = float(input())
    somaprec += preco[i]
    somapes += peso[i]
valor_tot = float(input())

print("peso =", somapes, "preco =", somaprec)
if somaprec != valor_tot:
    print("os valores monetarios estao em conflito")
else:
    print("nao ha conflito monetario")