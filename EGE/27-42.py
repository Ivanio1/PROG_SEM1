f=open('27-42a.txt')
n=int(f.readline())
s=0
summ=0
s1,s2=0,0
a=[]
r=1000000000
k=0
for i in range(n):
    a.append(list(map(int,f.readline().split())))
for i in range(n):
    s+=sum(a[i])
    a[i]=sorted(a[i])
#print(s)
for i in range(n):
    m=a[i][2]
    m1=a[i][0]
    s1+=m1
    summ+=m
    m2=a[i][1]
    s2+=m2
    if (m1+m2)%2!=0:
        k+=1

    for j in range(3):
        rr=m-a[i][j]
        if rr%2!=0:
            r=min(rr,r)
#if (s+summ)%2==0:
   # print(summ)
#else:
   # print(summ-r)
#print(s1,s2,summ,k)
p1=[10001]*2
p2=[10001]*2
X=[0]*4
for c in a:
    if (c[0]+c[2])%2!=0:
        X[0]=[p1[0],min(p1[1],c[2]-c[1])]
        X[1] = [min(p1[0], c[2] - c[0]),p1[1]]
        X[2] = [p2[0], min(p2[1], c[2] - c[1])]
        X[3] = [min(p2[0], c[2] - c[0]), p2[1]]
        t=min([z[0] for z in X])
        p1=[t,min([X[i][1]  for i in range(4) if X[i][0]==t ])]
        t = min([z[1] for z in X])
        p2 = [min([X[i][0] for i in range(4) if X[i][1] == t]),t]
print(summ-min(sum(p1),sum(p2)))
print(p1,p2,summ)
