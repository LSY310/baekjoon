n=input()
croatia=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatia:
    n=n.replace(i,"t")
print(len(n))