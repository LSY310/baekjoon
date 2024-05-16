n,x=map(int,input().split())
a=eval("["+input().replace(" ",",")+"]")
for k in a:
    if k<x:
        print(k, end=' ')