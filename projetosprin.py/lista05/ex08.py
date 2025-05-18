import random
v1 = [random.randint(0, 10) for i in range (75)]
v2 = [random.randint(0, 10) for i in range (75)]
v3 = [0 for i in range(75)]
for i in range (75):
    v3[i]= v1[i]+v2[i]
print(v3)