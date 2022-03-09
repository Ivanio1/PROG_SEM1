def F(a,x):
    l=0
    r=len(a)-1
    while l<r:
        c=(l+r)//2
        if x>a[c]:
            l=c+1
        else:
            r=c
    return a[l]==x
f = (open('26-53.txt'))
N = int(f.readline())
a=[]
b=[]

for i in range(N):
    c=int(f.readline())
    if c%2==0:
        a.append(c)
    b.append(c)
a.sort()
b.sort()
count=0
cmin=b[-1]+b[-2]+1
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        sred=(a[i]+a[j])//2
        if F(b,sred):
            count+=1
            cmin=min(cmin,sred)
print(count,cmin)