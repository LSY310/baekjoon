n=input().upper()
n_list=list(set(n))
count=[]
for i in n_list:
    c=n.count(i)
    count.append(c)
if(count.count(max(count)))>=2:
    print("?")
else:
    print(n_list[(count.index(max(count)))])