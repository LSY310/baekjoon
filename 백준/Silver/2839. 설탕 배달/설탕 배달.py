n=int(input())
check=0
if n%5==0:
    print(int(n/5))
else:
    for i in range(int(n/3)):
        if check==0:
            if (n%5+5*i)%3==0:
                check=1
                print(int(n/5)-i+int((n%5+5*i)/3))
    if check==0:
        print(-1)
