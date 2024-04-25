a,b=map(int,input().split())
c=int(input())
d=c%60
c=int(c/60)
h=a+c
m=d+b
if h>=24:
    h=h%24

if m>=60:
    if h==23:
        h=-1
    print(f"{h+1} {m-60}")
else:
    print(f"{h} {m}")