f=open('27-41a.txt')
n=int(f.readline())
s=0
a=[]
summ=0
r=1000000
for i in range(n):
    a.append(list(map(int,f.readline().split())))
for i in range(n):
    s+=sum(a[i])
#print(s)
for i in range(n):
    m=min(a[i])
    summ+=m
    for j in range(3):
        rr=a[i][j]-m
        if rr%2!=0:
            r=min(rr,r)
if (s+summ)%2!=0:
    print(summ)
else:
    print(summ+r)