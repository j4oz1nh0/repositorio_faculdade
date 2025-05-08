seg = int(input())
hr=0
min = 0
seug = 0
if seg>3600:
    hr = seg//3600
    min = seg%3600//60
    seug = seg%3600%60
    print(hr, min, seug)
if seg<3600 and seg>60:
    min = seg//60
    seug = seg%60
    print(hr, min, seug)
if seg<60:
    print(hr, min, seug)