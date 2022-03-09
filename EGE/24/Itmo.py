n = 0
A = []
for i in range(1, 100000):
    k = i
    maxx = 0
    base = 16
    if not (2 <= base <= 16):
        quit()
    newNum = ''
    while i > 0:
        newNum = str(i % base) + newNum
        i //= base
    print(newNum)
    a = (sum(map(int, list(newNum))))
    newNum = int(newNum)
    if newNum % 10 == newNum % 100 and a <= 10:
        A.append(newNum)
print(A)
