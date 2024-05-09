n=int(input())
m=[25,10,5,1]
for j in range(n):
    n2=int(input())
    for i in m:
        print(n2//i, end=' ')
        n2=n2%i