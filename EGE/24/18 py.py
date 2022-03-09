a = []
for s in open('18-k2.csv'):
    a.append(list(map(int, s.split(';'))))
n = len(a)
m = len(a[0])
b = [[1] * m for i in range(n)]
p = 1
while p == 1:
    p = 0
    for i in range(n):
        for j in range(m):
            x = 0
            if i > 0 and a[i - 1][j] < a[i][j] and x < b[i - 1][j]:
                x = b[i - 1][j]
            if i < n - 1 and a[i + 1][j] < a[i][j] and x < b[i + 1][j]:
                x = b[i + 1][j]
            if j > 0 and a[i][j - 1] < a[i][j] and x < b[i][j - 1]:
                x = b[i][j - 1]
            if j < m - 1 and a[i][j + 1] < a[i][j] and x < b[i][j + 1]:
                x = b[i][j + 1]
            if b[i][j] <= x:
                b[i][j] = x + 1
                p = 1
w = 0
for i in range(n):
    w = max(w, max(b[i]))
print(w)
