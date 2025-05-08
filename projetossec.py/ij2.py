i = 1
j = 7
temp = 7
indice=0
while i<=9:
    print(f"I={i} J={j}")
    j=j-1
    indice+=1
    if indice%3==0:
        j=temp+2
        temp = j
        i=i+2

