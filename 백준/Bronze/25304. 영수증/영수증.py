sum=int(input())
n=int(input())
t=0
for i in range(n):
    p,n2=map(int,input().split())
    t=t+p*n2
if t==sum:
    print("Yes")
else:
    print("No")
