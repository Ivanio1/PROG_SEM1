f=open('27-42b.txt')
n=int(f.readline())
s=[0]*3
k=0
rez=10**10
b=[10**10]*2
for i in range(n):
    a=list(map(int,f.readline().split()))
    a.sort()
    for j in range(3):
        s[j]+=a[j]
    #if (a[0]+a[1])%2!=0:
        #k+=1
    if (a[0]+a[2])%2!=0:
        m=a[2]-a[1]
        b.append(m)
        b.sort()
        b=b[:2]

print(s[2]-sum(b))