n=int(input())
a=[]
count=1
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort(key=lambda x: (x[1], x[0]))#뒷자리 기준 정렬
end=a[0][1]
for j in range(1,n):
    if a[j][0]>=end:
        end=a[j][1]
        count=count+1
print(count)