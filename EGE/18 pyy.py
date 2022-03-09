a = []
for i in open('18-2.csv'):
    a.append(list(map(int, i.split(';'))))
n = len(a)
m = len(a[0])
b = [[0] * m for i in range(n)]
b[0][0] = a[0][0] // 8
for j in range(1, m):
    b[0][j] = a[0][j] // 8 + b[0][j - 1]
for i in range(1, n):
    b[i][0] = a[i][0] // 8 + b[i - 1][0]
for i in range(1, n):
    for j in range(1, m):
        b[i][j] = min(b[i - 1][j], b[i][j - 1]) + a[i][j] // 8
print(b[-1][-1]*8)
