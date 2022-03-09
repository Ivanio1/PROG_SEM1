def Prostoe(N):
    a = int(N ** 0.5)
    for i in range(2, a + 1):
        if N % i == 0:
            return i
    return N


for i in range(113000000, 120000000 + 1, +2):
    j = i // 2
    p = int(j ** 0.5)
    if p ** 2 == j and p == Prostoe(p):
        print(i, p)
