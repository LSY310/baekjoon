a = []
b=[]
for i in range(28):
    b.append(int(input()))

for i in range(1, 31):
    if i not in b:
        a.append(i)


print(' '.join(map(str,a)))