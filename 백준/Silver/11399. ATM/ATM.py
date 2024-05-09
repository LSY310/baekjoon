n=int(input())
a=eval("["+input().replace(" ",",")+"]")
a2=a.sort()
c=0

for i in range(n):
    #c=c+sum(a[0:i])   
    c=c+sum(a[:i+1])
    
print(c)