f = open('k7b-2.txt')
s = f.readline()


def f(x):
    b = 'DBAC'
    a = x % 4
    return b[a]


c = 0
cmax = 0
for i in s:
    if i == f(c):
        c += 1
        cmax = max(c, cmax)
    else:
        if i == 'D':
            c = 1
        else:
            c = 0
print(cmax)
