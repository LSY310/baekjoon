n=int(input())
count=0
for i in range(n):
    re=1
    s=input()
    s_list=[]
    s_list.append(s[0])
    for j in range(1,len(s)):
        if s[j] in s_list:
            if s[j-1]==s[j]:
                pass
            else:
                re=0
                break
        else:
            s_list.append(s[j])
    if re==1:
        count=count+1
print(count)