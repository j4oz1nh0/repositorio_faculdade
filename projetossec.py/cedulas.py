a = int(input())
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
while a>=100:
    a=a-100
    cem +=1
if a>=50 and a<100:
    a = a-50
    cinq+=1
while a>=20 and a<50:
    a=a-20
    vinte +=1
if a>=10 and a<20:
    a = a-10
    dez+=1
if a>=5 and a<10:
    a = a-5
    cinco+=1
while a>=2 and a<5:
    a=a-2
    dois+=1
if a>=1 and a<2:
    a = a-1
    um+=1
print(cem, cinq, vinte, dez, cinco, dois, um)