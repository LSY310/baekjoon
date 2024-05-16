n=int(input())
a=eval("["+input().replace(" ",",")+"]")
a2=a.sort(reverse=True)
b=eval("["+input().replace(" ",",")+"]")
c=0
for i in range(n):
    c=c+a[i]*min(b)
    b[b.index(min(b))]=100
print(c)