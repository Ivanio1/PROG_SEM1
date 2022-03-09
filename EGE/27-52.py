f=open('27-52b.txt')
n=int(f.readline())
s=[[0]*3 for i in range(3)]
for i in range(n):
    x=int(f.readline())
    ostx=x%3
    s[ostx].append(x)
    s[ostx].sort()
    s[ostx]=s[ostx][1:]
c=s[0][2]+s[1][2]+s[2][2]
for i in range(3):
    c=max(c,sum(s[i]))
print(c)