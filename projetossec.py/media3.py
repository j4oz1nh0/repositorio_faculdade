N1, N2, N3, N4 = map(float,input().split())
media = (N1*2 + N2*3 + N3*4 + N4*1)/10
if media >= 5:
    if media < 7:
        print("Media: {:.1f}".format(media))
        print("Aluno em exame.")
        N5 = float(input())
        print("Nota do exame: {:.1f}".format(N5))
        mediafin = (media + N5)/2
        if mediafin >= 5:
            print("Aluno aprovado.")
            print("Media final: {:.1f}".format(mediafin))
        else:
            print("Aluno reprovado.")
            print("Media final: {:.1f}".format(mediafin))
    elif media >= 7:
        print("Media: {:.1f}".format(media))
        print("Aluno aprovado.")
else:
    print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")