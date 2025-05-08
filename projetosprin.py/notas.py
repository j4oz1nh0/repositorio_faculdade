
notas = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]
valor_total = notas
print(valor_total)
for cedulas in cedulas:
    quantidade = notas // cedulas
    print(f"{quantidade} nota(s) de R$ {cedulas},00")
    notas= notas%cedulas
