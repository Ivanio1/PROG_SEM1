f = open('24-157.txt')
s = f.readline()
a = [0] * 256
m = 0
b = ''
for i in range(len(s) - 2):
    if s[i + 1] == s[i + 2]:
        a[ord(s[i])] += 1
        if a[ord(s[i])] > m:
            m = a[ord(s[i])]
            b = s[i]
print(b, m)
