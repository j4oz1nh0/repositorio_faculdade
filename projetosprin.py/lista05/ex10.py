import random
v = [random.randint(1, 100) for i in range(100)]
a= int(input())
total=0
for i in range(len(v)):
    if v[i]==a:
        total+=1
print(total)