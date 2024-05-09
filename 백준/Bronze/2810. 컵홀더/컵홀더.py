n=int(input())
s=input()
s=s.replace("LL","C")
s="*"+"*".join(s)+"*"
s=s.replace("C","LL")
c=0
while 1:
    if s=="":
        break
    if s[0]=="*":
        s=s[2:]      
    elif s[1]=="*":
        s=s[2:]
    elif "*" not in s:
        break    
    else:
        s=s[1:]
        c=c+1
print(n-c)