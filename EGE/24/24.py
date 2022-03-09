f = (open('zadanie24_2 (6).txt'))
s = f.readline()
c = 1
cmax = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1] and s[i] == 'D':
        c += 1
        cmax = max(c, cmax)
    else:
        c=1
print(cmax)
