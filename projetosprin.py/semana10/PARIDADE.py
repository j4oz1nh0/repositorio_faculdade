a = input()
num1 = 0
for i in range(len(a)):
    if a[i]=="1":
        num1+=1
if num1%2==0:
    print(f"{a}0")
else:
    print(f"{a}1")