n = str(input())
a = n.split('-')

result = 0

x = sum(map(int, (a[0].split('+'))))
if n[0] == '-':
    result= result - x
else:
    result = result + x

for x in a[1:]: 
    x = sum(map(int, (x.split('+'))))
    result = result - x
print(result)