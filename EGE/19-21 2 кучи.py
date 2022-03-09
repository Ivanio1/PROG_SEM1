a = [[0] * 100 for i in range(100)]
for i in range(40, 0, -1):
    for j in range(40, 0, -1):
        if i + j >= 40:
            a[i][j] = 0
        else:
            p = [a[i + 1][j], a[i][j + 1], a[i * 2][j], a[i][j * 2]]
            n = [x for x in p if x <= 0]
            if n:
                a[i][j] = -max(n) + 1
            else:
                a[i][j] = -max(p)
for i in range(1,30):
    print(i,a[9][i])
print(a.count(-2))
