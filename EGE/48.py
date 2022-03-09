f = open('zadanie24_1 (6).txt')
s = f.readline()
n = 1
nmax = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1] and s[i] == 'C':
        n += 1
        nmax = max(nmax, n)
    else:
        n = 1
print(nmax)
