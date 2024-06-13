
n=input()
if '0' in n:
    n=sorted(n,reverse=True)
    sum=0
    for i in n:
        sum=sum+int(i)
    if sum%3==0:
        print(''.join(n))
    else :
        print(-1)
else:
    print(-1)