n=int(input())
if n%10!=0:
    print(-1)
    #300,60,10
elif n%300==0:
    print(f"{int(n/300)} 0 0")
else:
    a=int(n/300)
    n=n%300
    b=int(n/60)
    c=int((n%60)/10)
    print(f"{a} {b} {c}")