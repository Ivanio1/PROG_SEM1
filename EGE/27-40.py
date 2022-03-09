f=open('27-40b.txt')
n=int(f.readline())
s=0
a=[]
summ=0
r=1000000
for i in range(n):
    a.append(list(map(int,f.readline().split())))
for i in range(n):
    s+=sum(a[i])
for i in range(n):
    m=max(a[i])
    summ+=m
    for j in range(3):
        rr=m-a[i][j]
        if rr%2!=0:
            r=min(rr,r)
if (s+summ)%2!=0:
    print(summ)
else:
    print(summ-r)

