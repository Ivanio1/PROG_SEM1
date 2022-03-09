f = (open('47.txt'))
N = int(f.readline())
a=[]
for i in range(N):
    a.append(int(f.readline()))
a.sort()
count=0
cmax=0
n=len(a)
for i in range(n-1):

    for j in range(i+1,n):
        sred=(a[i]+a[j])//2
        c = 0
        for x in range(n):
            if a[x]<=sred:
                c+=1
        if c!=0 and c%3==0:
            count+=1
            cmax=max(cmax,c)
print(cmax,count)
