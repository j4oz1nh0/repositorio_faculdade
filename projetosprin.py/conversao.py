S = int(input())
if S < 60:
    print(f"0:0:{S}")
if S >= 60 and S < 3600:
    M = S // 60
    S = S % 60
    print(f"0:{M}:{S}")
if S >= 3600:
    M = S // 60
    H = M // 60
    M = M % 60
    S = S % 60
    print(f"{H}:{M}:{S}")
