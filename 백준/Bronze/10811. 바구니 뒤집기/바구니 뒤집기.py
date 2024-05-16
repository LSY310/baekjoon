n, m = map(int, input().split())
a = list(range(1, n+1))

for _ in range(m):
    x, y = map(int, input().split())
    a[x-1:y] = list(reversed(a[x-1:y]))

print(" ".join(map(str, a)))