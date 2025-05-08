soma_media = input()
matriz = [[float(input()) for j in range(12)] for i in range(12)]
soma = 0.0
media = 0.0
regra=11
for i in range(6, 11):
        for j in range(i+1, 12):
            if soma_media == 'S':
                soma = soma + matriz[i][j]
            if soma_media == 'M':
                media = media + matriz[i][j]
for i in range(1, 6):
        for j in range(regra, 12):
            if soma_media == 'S':
                soma = soma + matriz[i][j]
            if soma_media == 'M':
                media = media + matriz[i][j]
        regra= regra-1
if soma_media == 'S':
    print("{:.1f}".format(soma))
if soma_media == 'M':
    media = media/66
    print("{:.1f}".format(media))
