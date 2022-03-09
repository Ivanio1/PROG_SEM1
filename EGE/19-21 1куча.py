a = [0] * 400
for i in range(100, 0, -1):
    if i>=30:
        a[i]=0
    else:
        if a[i + 2] > 0 and a[i + 3] > 0 and a[2 * i] > 0:
            a[i] = -max(a[i + 2], a[i + 3], a[i * 2])
        else:
            m = -1000
            for j in [a[i + 2], a[i + 3], a[i * 2]]:
                if j <= 0 and j > m:
                    m = j
            a[i] = -m + 1
for i in range(30):
    print(i, a[i])
n = 0
print(a.count(2))


