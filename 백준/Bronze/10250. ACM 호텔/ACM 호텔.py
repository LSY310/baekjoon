n=int(input())
for i in range(n):
    h,w,m=map(int,input().split())
    x=m%h
    y=m//h+1
    if x==0:
        x=h
        y=y-1
    if y<10:
        print(f"{x}0{y}")
    else:
        print(f"{x}{y}")