a = {}
for i in range(2943444, 2943529 + 1):
    num = 0
    for j in range(1, i + 1):
        if i % j == 0:
            num += 1
            if num > 2: break
            a[num] = j
    if num == 2:
        print(a[1], a[2])
