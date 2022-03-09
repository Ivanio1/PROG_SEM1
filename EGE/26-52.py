def sred(x,y):
    return (x+y)/2

f=open('26-52.txt')
N=int(f.readline())
a=[]
for i in range(N):
    a.append(int(f.readline()))
a.sort()

n=len(a)
c=0
cmin=a[1]+a[-1]
for i in range(n-1):
    for j in range(i+1,n):
        if j-i-1<=100:   #!!!!!!!!!!
            if (a[i]+a[j])%10==0:
                c+=1
                cmin=min(cmin,sred(a[i],a[j]))
print(c,cmin)
