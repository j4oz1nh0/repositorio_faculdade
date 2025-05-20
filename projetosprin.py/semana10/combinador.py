a=  int(input())
for i in range(a):
    palavra1, palavra2 = input().split()
    palavra=''
    if len(palavra1)>len(palavra2):
        for i in range(len(palavra2)):
            palavra+=palavra1[i]+palavra2[i]
        for i in range(len(palavra2), len(palavra1)):
            palavra+=palavra1[i]
    if len(palavra1)<len(palavra2):
        for i in range(len(palavra1)):
            palavra+=palavra1[i]+palavra2[i]
        for i in range(len(palavra1), len(palavra2)):
            palavra+=palavra2[i]
    if len(palavra1)==len(palavra2):
        for i in range(len(palavra1)):
            palavra += palavra1[i] + palavra2[i]
    print(palavra)


