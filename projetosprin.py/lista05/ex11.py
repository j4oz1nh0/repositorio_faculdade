import random
vtemp = [random.randint(15, 40) for i in range (121)]
media = 0
t20 = 0
t35 = 0
menor=0
for i in range (121):
    media+=vtemp[i]
    if vtemp[i]>35:
        t35+=1
    elif vtemp[i]<20:
        t20+=1
media = media/len(vtemp)
for i in range (121):
    if vtemp[i]<media:
        menor+=1
print("{:.1f}".format(media))
print(menor)
print(t20)
print(t35)